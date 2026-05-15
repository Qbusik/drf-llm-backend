from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PromptJob
from .serializers import PromptSerializer
from .tasks import process_prompt


class PromptView(APIView):

    def post(self, request):

        serializer = PromptSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        prompt = serializer.validated_data["prompt"]

        job = PromptJob.objects.create(prompt=prompt)

        process_prompt.delay(str(job.id))

        return Response({"job_id": job.id, "status": job.status})


class PromptStatusView(APIView):

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
