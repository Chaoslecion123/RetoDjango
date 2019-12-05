from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from retoDjango import settings

@shared_task
def send_emails_users(email,subjet,message):
    correo = email
    asunto = subjet
    mensaje = message

    users = User.objects.all()

    for user in users:
        send_mail(
            asunto,
            mensaje,
            correo,
            [user.email],
            fail_silently=False
        )

    return 'el mensaje se envio exitosamente'
