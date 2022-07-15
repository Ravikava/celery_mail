from celery.app import shared_task , task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from time import sleep
from django.core.mail import send_mail

logger = get_task_logger(__name__)

@shared_task(name='send_email_task')
def send_mail_task():
    
    subject = "TEST"
    msg = "This Is a test message"
    
    send_mail(
        subject=subject,
        message = msg,
        from_email = "kavaravi2@gmail.com",
        recipient_list = ["patelharshu8768@gmail.com"]
    )