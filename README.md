# SGH – Sistema de Gestión Hotelera

Sistema web para el **Apart Hotel del Centro** (23 habitaciones y 11 departamentos = 34 unidades).
Tiene control de acceso por roles (Gerente, Recepcionista, Housekeeping, Mantenimiento) y un
portal público donde los huéspedes reservan y consultan su reserva con un código.

**Tecnologías:** Python 3.12+, Django 5.2 (LTS), MySQL (lo administramos con MySQL Workbench), Git y GitHub.

**Fuera de alcance:** facturación electrónica y funciones fiscales (ARCA/AFIP). Solo registramos cobros
y medios de pago (efectivo, transferencia, posnet).

> Estado actual: **Sprint 0**. Está armada la estructura base: login, roles y una página
> "En construcción" por módulo. La lógica de cada módulo se programa en los próximos sprints.

---

## ¿Qué es Django?

Django es un framework de Python para hacer aplicaciones web. Organiza el código con el patrón **MTV**:

- **Modelo** (`models.py`) = una **tabla** de la base de datos, escrita como una clase de Python.
- **Vista** (`views.py`) = la **lógica**: recibe el pedido del navegador, busca o guarda datos y elige qué mostrar.
- **Template** (`templates/*.html`) = el **HTML** que ve el usuario, con huecos que completa la vista.
- **URL** (`urls.py`) = la **dirección** del navegador que dispara cada vista (por ejemplo `/reservas/`).

Recorrido de un pedido: el navegador pide `/reservas/` → `urls.py` encuentra la vista → la vista usa
los modelos → devuelve un template con los datos.

---

## Mapa de carpetas

```
SGH/
├── manage.py             ← herramienta de comandos de Django (runserver, migrate, test...)
├── requirements.txt      ← librerías que hay que instalar
├── .env.example          ← modelo del archivo .env (configuración y contraseñas)
├── .gitignore            ← lo que NO se sube a GitHub
├── README.md             ← este archivo
├── sgh/                  ← configuración del proyecto
│   ├── settings.py       ←   apps instaladas, base de datos, idioma, login...
│   ├── urls.py           ←   rutas principales (incluye las de cada app)
│   ├── views.py          ←   vista "inicio" (página principal después del login)
│   └── wsgi.py, asgi.py  ←   para publicar el sitio en un servidor (no se tocan)
├── usuarios/             ← Módulo 1: usuarios, roles y login (RF-01 a RF-04)
├── unidades/             ← Módulos 2 y 3: habitaciones, departamentos, tarifas, promociones y tablero de estado (RF-05 a RF-14)
├── reservas/             ← Módulo 4: reservas internas y disponibilidad (RF-15 a RF-19)
├── portal/               ← Módulo 5: portal público de reservas para huéspedes (RF-20 a RF-24)
├── huespedes/            ← Módulo 6: huéspedes, check-in, consumos y check-out (RF-25 a RF-32)
├── caja/                 ← Módulo 7: cobros, medios de pago, turnos y arqueo (RF-33 a RF-37)
├── pedidos/              ← Módulo 8: pedidos y reclamos para Housekeeping o Mantenimiento (RF-38 a RF-41)
├── reportes/             ← Módulo 9: reportes para el Gerente (RF-42 a RF-45)
├── templates/            ← HTML compartidos
│   ├── base.html         ←   plantilla base (barra de navegación, mensajes)
│   ├── inicio.html       ←   página principal con tarjetas por módulo
│   └── registration/login.html ← formulario de login
└── static/               ← CSS, JavaScript e imágenes propias
    ├── css/estilos.css
    ├── js/
    └── img/
```

Cada app (carpeta de módulo) tiene siempre los mismos archivos:

| Archivo | Para qué sirve |
|---|---|
| `models.py` | Las tablas del módulo (por ahora solo un comentario con las entidades previstas). |
| `views.py` | Las vistas (funciones) del módulo. |
| `urls.py` | Las direcciones del módulo (`/reservas/`, `/reservas/nueva/`...). |
| `forms.py` | Los formularios del módulo. |
| `admin.py` | Qué tablas se ven en el panel `/admin/`. |
| `tests.py` | Las pruebas automáticas del módulo. |
| `migrations/` | Archivos que genera Django para crear o cambiar tablas. **No se editan a mano.** |
| `templates/<app>/` | Los HTML del módulo. |

En `usuarios/` hay además `decorators.py`, con el decorador `rol_requerido` que controla qué rol entra a cada vista.

### Quién ve qué

| Módulo | Gerente | Recepcionista | Housekeeping | Mantenimiento |
|---|:-:|:-:|:-:|:-:|
| Usuarios | ✔ | | | |
| Unidades | ✔ | ✔ | ✔ | ✔ |
| Reservas | ✔ | ✔ | | |
| Huéspedes | ✔ | ✔ | | |
| Caja | ✔ | ✔ | | |
| Pedidos | ✔ | ✔ | ✔ | ✔ |
| Reportes | ✔ | | | |
| Portal | público (sin login) | | | |

La lista de módulos del menú está en `MODULOS` (`usuarios/models.py`) y el permiso real de cada vista
en su `@rol_requerido(...)`. Si se cambia uno, hay que cambiar el otro.

---

## Instalación paso a paso

### Antes de empezar

Tener instalado: **Python 3.12 o superior**, **Git**, **MySQL Server** y **MySQL Workbench**.

### Windows (PowerShell)

```powershell
# 1. Clonar el repositorio y entrar a la carpeta
git clone https://github.com/osidev23/SGH.git
cd SGH

# 2. Crear el entorno virtual (una carpeta "venv" con las librerías del proyecto)
python -m venv venv

# 3. Activarlo (aparece "(venv)" al principio de la línea)
venv\Scripts\activate
#    Si PowerShell no deja ejecutar scripts, correr una sola vez:
#    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# 4. Instalar las librerías
pip install -r requirements.txt
```

**5. Crear la base de datos** en MySQL Workbench (abrir una pestaña de consulta y ejecutar):

```sql
CREATE DATABASE sgh CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

> El usuario de MySQL que usen tiene que poder crear bases, porque `python manage.py test`
> crea una base temporal llamada `test_sgh` (con `root` no hay problema).

```powershell
# 6. Copiar el archivo de configuración y completarlo con tu usuario y contraseña de MySQL
copy .env.example .env
#    Abrir .env y cambiar DB_USER, DB_PASSWORD y SECRET_KEY.
#    Para generar una SECRET_KEY nueva:
#    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 7. Crear las tablas en la base
python manage.py migrate

# 8. Crear tu usuario administrador (se considera Gerente, ve todo)
python manage.py createsuperuser

# 9. Levantar el servidor
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/> en el navegador e iniciar sesión.
Los demás usuarios (con su rol) se crean desde <http://127.0.0.1:8000/admin/>.

### Linux / Mac

Los pasos son los mismos, cambian estos comandos:

```bash
python3 -m venv venv
source venv/bin/activate
cp .env.example .env
```

`mysqlclient` necesita librerías del sistema antes de hacer `pip install`:

- **Ubuntu/Debian:** `sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config`
- **Mac (Homebrew):** `brew install mysql-client pkg-config`

---

## Comandos de uso diario

Siempre con el entorno virtual activado (`(venv)` al principio de la línea):

| Comando | Qué hace |
|---|---|
| `python manage.py runserver` | Levanta el sistema en <http://127.0.0.1:8000/>. Se corta con Ctrl+C. |
| `python manage.py makemigrations` | Después de cambiar un `models.py`: genera los archivos de migración. |
| `python manage.py migrate` | Aplica las migraciones: crea o modifica las tablas en MySQL. |
| `python manage.py test` | Corre todas las pruebas. `python manage.py test reservas` corre solo las de una app. |
| `python manage.py createsuperuser` | Crea un usuario administrador. |

---

## Cómo trabajamos con Git y GitHub

**Ramas:**

- `main` → versión **estable**. Nadie trabaja directo acá.
- `develop` → rama de **integración**: acá se juntan las tareas terminadas.
- `feature/<modulo>-<descripcion>` → una rama **por tarea**. Ej.: `feature/reservas-formulario-alta`.

**Flujo de una tarea:**

```bash
# 1. Partir siempre de develop actualizado
git checkout develop
git pull

# 2. Crear la rama de la tarea
git checkout -b feature/reservas-formulario-alta

# 3. Trabajar y hacer commits cortos, en español, con el módulo adelante
git add .
git commit -m "reservas: agrega formulario de alta"

# 4. Subir la rama a GitHub
git push -u origin feature/reservas-formulario-alta
```

5. En GitHub, abrir un **Pull Request** hacia `develop`.
6. **Otro integrante** lo revisa (lo prueba y comenta). Cuando lo aprueba, se hace el merge.
7. Cuando `develop` está estable (por ejemplo, al cerrar un sprint), se pasa a `main`.

Antes de abrir el Pull Request: correr `python manage.py test` y verificar que todo pase.

---

## Convenciones del equipo

- **Todo en español:** nombres de apps, modelos, campos, vistas, templates, comentarios y commits
  (sin tildes ni ñ en los nombres de código: `huespedes`, `TurnoCaja`, `anio`).
- **Una app por módulo.** Cada cosa va en la app de su módulo; no se crean apps ni carpetas nuevas sin acordarlo.
- **Vistas basadas en funciones** (`def mi_vista(request):`), protegidas con `@login_required` y
  `@rol_requerido(...)`. Excepción: el login/logout, que usa las vistas que ya trae Django.
- **Nunca se borra un registro:** cada modelo tiene un campo `activo = models.BooleanField(default=True)`
  y para "borrar" se pone en `False` (baja lógica). Los listados muestran solo los activos.
- **Templates** de cada app en `<app>/templates/<app>/` y siempre con `{% extends "base.html" %}`.
- **No se sube el `.env`** ni la carpeta `venv/` (ya están en `.gitignore`).
- **Migraciones:** se generan con `makemigrations` y se suben al repo; no se editan a mano.
