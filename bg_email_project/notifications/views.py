from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .tasks import send_welcome_email

def register(request):
    print("🔥 Inside the register view!")  # Debug: check if view is hit
    
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            print("🔥 Calling Celery task to send email to:", user.email)  # Debug here
            send_welcome_email.delay(user.email)

            messages.success(request, 'Your account has been created! Check your email for a welcome message.')
            form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
