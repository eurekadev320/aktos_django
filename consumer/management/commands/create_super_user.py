from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('aktos', 'aktos@admin.com', 'aktos')
