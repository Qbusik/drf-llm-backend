from celery import shared_task

from .models import PromptJob
from .llm import ask_llm


@shared_task(autoretry_for=(Exception,), retry_backoff=True, max_retries=5)
def process_prompt(job_id, messages):
    job = PromptJob.objects.get(id=job_id)

    try:
        response = ask_llm(messages)

        job.response = response
        job.status = "DONE"
        job.save()

    except Exception as e:
        job.status = "FAILED"
        job.error = str(e)
        job.save()
