from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        # Obtén el grupo con id 2
        default_group = Group.objects.get(id=1)  # O bien, usa .filter(name="usuarios").first() para mayor claridad
        # Añade el usuario al grupo
        instance.groups.add(default_group)