from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(user_email):
    logger.info(f"📤 Sending email to {user_email}")
    
    subject = 'Welcome to Our Service'
    message = 'Thanks for signing up. We are glad to have you!'
    from_email = 'yosefenadagim@gmail.com'
    recipient_list = [user_email]

    result = send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    logger.info(f"✅ Email sent result: {result}")

    return f"Sent welcome email to {user_email}"
