from celery import shared_task

from .models import PromptJob
from .llm import ask_llm


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=5)
def process_prompt(self, job_id):

    job = PromptJob.objects.get(id=job_id)

    try:
        job.status = "PROCESSING"
        job.save()

        answer = ask_llm(job.prompt)

        job.response = answer
        job.status = "DONE"
        job.save()

    except Exception as e:

        job.status = "ERROR"
        job.error = str(e)
        job.save()

        raise
