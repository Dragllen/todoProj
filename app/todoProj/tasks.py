from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command 


logger = get_task_logger(__name__)

# NEW
@shared_task
def check_deadline():
    call_command("check_deadline", )


# NEW
@shared_task
def send_email_report():
    call_command("email_report", )
