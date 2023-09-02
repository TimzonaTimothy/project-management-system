from django.conf import settings
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
import secrets
from .models import Project

def get_random_string(length=8, allowed_chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    project_id = ''.join(secrets.choice(allowed_chars) for i in range(length))
    if Project.objects.filter(project_id=project_id).exists():
        project_id = get_random_string()
    return str(project_id)

def generate_project_id(sender, instance, created, **kwargs):
    if created:
        instance.project_id = get_random_string()
        instance.save()

post_save.connect(generate_project_id, sender=Project)