from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to Our Service'
    message = 'Thanks for signing up. We are glad to have you!'
    from_email = 'your_email@gmail.com'
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Sent welcome email to {user_email}"
