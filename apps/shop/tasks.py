from celery import shared_task
from django.core.mail import send_mail
from django.http import HttpResponse

@shared_task
def send_email_task():
    send_mail(
        'test',  # Тема письма
        'привет. теперь ты будешь получать спам',  # Тело письма
        'dastiw1910@gmail.com',  # Адрес отправителя
        ['edilbekova_aiperi@mail.ru'],  # Список адресов получателей
        fail_silently=False,  # Если установлено значение True, ошибки отправки будут игнорироваться
    )
    return HttpResponse('Email sent successfully!')
