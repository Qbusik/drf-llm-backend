from drf_spectacular.utils import extend_schema, OpenApiParameter
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
                    "job_id": {"type": "string"},
                    "status": {"type": "string"},
                },
            }
        },
        summary="Create LLM prompt job",
        description="Creates async LLM job and returns job_id",
        tags=["LLM"],
    )
    def post(self, request):

        serializer = PromptSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        prompt = serializer.validated_data["prompt"]

        job = PromptJob.objects.create(prompt=prompt)

        process_prompt.delay(str(job.id))

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
