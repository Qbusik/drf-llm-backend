from django.urls import path

from .views import (
    PromptView,
    PromptStatusView,
    login_page,
    chat_page,
    register_page,
)

app_name = "chat"

urlpatterns = [
    path("prompt/", PromptView.as_view()),
    path("prompt/<uuid:job_id>/", PromptStatusView.as_view()),
    path("login/", login_page, name="login-page"),
    path("", chat_page, name="chat-page"),
    path("register/", register_page, name="register-page"),
]
