# 🤖 DRF LLM Backend 🤖

Simple Django REST API application for interacting with a Large Language Model (Gemini).  
The project provides authentication, asynchronous processing with Celery, and a minimal frontend for testing chat functionality.

---

## 📃 Features

- 🔐 JWT Authentication
- 💬 Chat with LLM (Gemini API integration)
- ⚙️ Asynchronous processing using Celery
- 📊 Job status tracking (PENDING / DONE / FAILED)
- 🌐 Simple HTML frontend (login + chat interface)
- 📡 REST API endpoints for integration
- 🧠 Chat history handled on frontend side

---

## 🚀 Run with DOCKER

This is the fastest method to get the project running in an isolated environment.

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
    The application will be available at: `http://localhost:8000/`