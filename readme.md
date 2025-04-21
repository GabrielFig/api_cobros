# 💸 FastAPI Billing System

Este proyecto es una API RESTful construida con **FastAPI** y **PostgreSQL** para gestionar clientes, facturas y transacciones. Es ideal como base para sistemas de facturación, análisis financiero o CRM.

---

## 🚀 Características

- 🔐 Autenticación opcional (JWT o básica - opcional)
- 👥 Gestión de clientes (`/customers`)
- 🧾 Gestión de facturas (`/invoices`)
- 💳 Gestión de transacciones (`/transactions`)
- 📊 Estructura preparada para escalar con modularidad
- 📄 Documentación automática con Swagger y ReDoc

---

## 🧱 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/) (sobre SQLAlchemy)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## ⚙️ Requisitos

- Python 3.10+
- Docker & Docker Compose
- `pipenv` o `pip`

---

## 🛠️ Instalación local

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/fastapi-billing.git
cd fastapi-billing
```
### 2. Crea un archivo .env

```bash
DB_HOST=localhost
DB_PORT=5411
DB_NAME=test1
DB_USER=test_user
DB_PASSWORD=test_password
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```
### 4. Corre la aplicación

```bash
uvicorn app.main:app --reload
```

