# 🌐 Proyecto Web: Arca Oexdi

Desarrollo de la página web oficial de **Arca Oexdi**, con arquitectura escalable, segura y modular. El proyecto se compone de un backend en **Django REST Framework** y un frontend en **Angular**, alojado en **GitHub** y desplegado en **Hostinger**.

---

## 🧰 Tecnologías utilizadas

| Capa       | Lenguaje / Framework     | Descripción técnica |
|------------|---------------------------|----------------------|
| Backend    | Python + FastApi      | API RESTful, lógica empresarial, autenticación |
| Frontend   | REAC      | SPA dinámica, componentes reutilizables |
| Control de versiones | Git + GitHub     | Repositorios separados para backend y frontend |
| Hosting    | Hostinger (vía GitHub)    | Despliegue automatizado y escalable |

---

## 📁 Estructura del proyecto

00_pagina_web_arcaoexdi/ ├── backend_django/ # API REST con Django │ ├── env/ # Entorno virtual Python │ ├── arcaoexdi_core/ # Proyecto Django │ └── manage.py ├── frontend_angular/ # Aplicación Angular │ └── src/ └── README.md # Documentación principal

Código

---

## ⚙️ Instalación del entorno backend (Django)

```bash
# Crear entorno virtual
cd backend_django
python3 -m venv env
source env/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install django djangorestframework python-decouple django-cors-headers drf-yasg pytz

# Crear archivo de requerimientos
pip freeze > requirements.txt

# Iniciar proyecto Django
django-admin startproject arcaoexdi_core .
⚙️ Instalación del entorno frontend (Angular)
bash
# Instalar Angular CLI (si no lo tienes)
npm install -g @angular/cli

# Crear proyecto Angular
cd frontend_angular
ng new arcaoexdi_front --routing --style=scss

# Instalar dependencias útiles
npm install axios bootstrap ngx-toastr
🔐 Seguridad y escalabilidad
Uso de variables de entorno con python-decouple

CORS habilitado para conexión segura con Angular

Autenticación con tokens (JWT)

Documentación Swagger con drf-yasg

Componentes Angular desacoplados y reutilizables

📄 Documentación técnica
Toda la documentación del proyecto estará disponible en:

README.md principal

Carpeta docs/ (opcional) con diagramas de arquitectura, flujos de API y scripts de despliegue

Swagger UI (/swagger/) para explorar la API REST

🚀 Despliegue
El proyecto será alojado en Hostinger, con integración continua desde GitHub. Cada cambio en main será desplegado automáticamente.

🤝 Colaboración
Este proyecto está diseñado para ser modular, replicable y colaborativo. Si deseas contribuir:

Clona el repositorio

Crea una rama con tu mejora

Abre un Pull Request explicando tu aporte

📌 Autor
Arca Oexdi Desarrollador especializado en Python, Django REST y entornos escalables. 

Credenciales Admin Django
User Arcaoexdi
Email arcaoexdi@gmail.com
Password Arcaoexdi963/+
