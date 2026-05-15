from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PromptJob
from .serializers import PromptSerializer
from .tasks import process_prompt


class PromptView(APIView):

    @extend_schema(
        request=PromptSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "job_id": {"type": "string", "format": "uuid"},
                    "status": {"type": "string"},
                },
            }
        },
        examples=[
            OpenApiExample(
                "Chat request example",
                value={
                    "messages": [
                        {"role": "user", "content": "Hello"},
                        {"role": "assistant", "content": "Hi! How can I help?"},
                    ]
                },
                request_only=True,
            )
        ],
        summary="Create LLM prompt job",
        description=(
            "Creates async LLM job.\n\n"
            "IMPORTANT:\n"
            "- You must send `messages` as a list of objects\n"
            "- Each message must contain: role + content\n"
            "- Supported roles: user, assistant\n"
        ),
        tags=["LLM"],
    )
    def post(self, request):

        serializer = PromptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        messages = serializer.validated_data["messages"]

        job = PromptJob.objects.create(status="PENDING")

        process_prompt.delay(str(job.id), messages)

        return Response({"job_id": job.id, "status": job.status})


class PromptStatusView(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="job_id",
                type=str,
                location=OpenApiParameter.PATH,
                description="ID of the LLM job",
            )
        ],
        responses={
            200: {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "status": {"type": "string"},
                    "response": {"type": "string", "nullable": True},
                    "error": {"type": "string", "nullable": True},
                },
            }
        },
        summary="Get LLM job status",
        tags=["LLM"],
    )
    def get(self, request, job_id):

        job = PromptJob.objects.get(id=job_id)

        return Response(
            {
                "id": job.id,
                "status": job.status,
                "response": job.response,
                "error": job.error,
            }
        )


def login_page(request):
    return render(request, "login.html")


def chat_page(request):
    return render(request, "chat.html")


def register_page(request):
    return render(request, "register.html")
