from django.core.mail import send_mail

from ForgottenPhotocards import settings
from ForgottenPhotocards.celery import app
from channelparser import entrypoint


@app.task
def update_posts(token: str = None):
    entrypoint(token)


@app.task
def send_email_to_author(message: str, email: str):
    send_mail("Форма обратной связи с сайта забытые фотокарточки", message, settings.EMAIL_HOST_USER,
              [settings.EMAIL_HOST_USER, email], fail_silently=False)
