# Auth Service

This is a Django-based authentication service built as part of my microservice backend project.

This service is responsible for handling user authentication and generating JWT tokens.

---

## What this service does

* User registration and login
* Generate JWT tokens
* Validate users
* Acts as central authentication service for other services

---

## How it works

* Auth Service creates JWT token using **private key**
* Other services (Skill, Review, Notification) verify token using **public key**

---

## Tech Used

* Python
* Django
* Django REST Framework
* JWT (RS256)
* Docker

---

## Project Structure

```text
AuthService/
│
├── myapp/              # App logic (auth, models, serializers)
├── authservice/        # Main Django project
├── jwt_key/            # JWT keys (ignored)
├── manage.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

---

## API (basic)

* POST `/register/` → create user
* POST `/login/` → get JWT token

---

## How to Run

### 1. Clone

```bash
git clone https://github.com/YOUR-USERNAME/AuthService_labora.git
cd AuthService
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Run server

```bash
python manage.py runserver
```

---

## Run with Docker

```bash
docker build -t auth-service .
docker run -p 8000:8000 auth-service
```

---

## Security Notes

* `private.pem` is never uploaded
* `jwt_key/` folder is ignored
* `.env` is ignored

---

