# 🤖 DRF LLM Backend 🤖

Simple Django REST API application for interacting with a Large Language Model (Gemini).  
The project provides authentication, asynchronous processing with Celery, and a minimal frontend for testing chat functionality.

---

## 📃 Features

- JWT Authentication (SimpleJWT)
- Chat with LLM (Google Gemini API)
- Asynchronous processing with Celery + Redis
- Job tracking (PENDING / SUCCESS / FAILED)
- REST API for integration with external clients
- Simple frontend for testing authentication and chat
- Rate limiting (throttling) for LLM requests

---

## 🧱 Tech Stack

- Python 3.12
- Django + Django REST Framework
- Celery
- Redis
- PostgreSQL
- Gunicorn
- Docker + Docker Compose

---

## 🚀 Run with DOCKER

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Qbusik/drf-llm-backend.git
    ```

2.  **Configure Environment Variables:**

    ```bash
    cp .env.sample .env
    # then fill in your credentials
    ```

3.  **Build and Run Containers:**
    ```bash
    docker-compose up --build
    ```