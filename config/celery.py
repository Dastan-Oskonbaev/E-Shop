import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.broker_transport_options = {
    'data_folder_in': 'C:/Users/Dastan/Desktop/E_Shop/celery/queues',
    'data_folder_out': 'C:/Users/Dastan/Desktop/E_Shop/celery/queues',
}

app.conf.beat_schedule = {
    'send_email_task': {
        'task': 'apps.blog.tasks.send_email_task',
        'schedule': 30.0,
        'kwargs': {},
    }
}
