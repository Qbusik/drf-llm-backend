from django.urls import path

from .views import (
    PromptView,
    PromptStatusView,
)

app_name = "chat"

urlpatterns = [
    path("prompt/", PromptView.as_view()),
    path("prompt/<uuid:job_id>/", PromptStatusView.as_view()),
]
