from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_welcome_email(email):
    print(f"📨 Celery task running to send email to: {email}")  # Debug print to confirm task is triggered
    
    result = send_mail(
        'Welcome to Our Platform',
        'Thanks for signing up!',
        'youremail@example.com',  # Use a valid sender email here
        [email],
        fail_silently=False,
    )
    
    print(f"📬 Email send result: {result}")  # Check result of email sending
    return f"Sent welcome email to {email}, result: {result}"
