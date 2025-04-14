Here’s the updated `README.md` with a more detailed setup guide for registering users and sending emails, including the modifications we made for the registration form:

```markdown
# 📧 Background Email Notification System with Django & Celery

This project demonstrates how to send email notifications in the background using **Django**, **Celery**, and **Redis**. It's perfect for offloading long-running tasks like sending welcome emails, order confirmations, or scheduled reports.

---

## 🚀 Tech Stack

- **Backend:** Django
- **Task Queue:** Celery
- **Broker & Result Backend:** Redis
- **Email Service:** SMTP (Gmail)
- **Python Version:** 3.10+
- **Virtual Environment:** venv

---

## 🛠️ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/TewodrosAdimas/bg_email_project.git
cd bg_email_project
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Update your `settings.py` with the following email config:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

> ⚠️ Use Gmail App Passwords if 2FA is enabled.

---

## 🧪 Run the Project

### 1. Start Redis Server

```bash
redis-server
```

### 2. Run Django Server

```bash
python manage.py runserver
```

### 3. Start Celery Worker

```bash
celery -A bg_email_project worker --loglevel=info
```

---

## 📝 Registration Form and Email Notification

This project includes a **registration form** that sends a **welcome email** to the user once they successfully register. 

1. **Visit the registration page**: `http://127.0.0.1:8000/accounts/register/`
2. **Submit the registration form** with valid details.
3. **A welcome email** will be sent to the registered email address via the Celery background task.

---

## 🔁 Send Test Email

You can trigger an email using the Django shell:

```bash
python manage.py shell
```

```python
from notifications.tasks import send_welcome_email
send_welcome_email.delay('recipient@example.com')
```

---

## 📦 Project Structure

```
bg_email_project/
│
├── bg_email_project/        # Main Django settings
├── notifications/           # App for background tasks
│   ├── tasks.py             # Celery tasks for sending emails
│
├── manage.py
├── requirements.txt
```

---

## 📄 License

MIT License

---

## 🤝 Contributing

PRs and ideas are welcome! Feel free to fork this project and make it your own.

---

```

