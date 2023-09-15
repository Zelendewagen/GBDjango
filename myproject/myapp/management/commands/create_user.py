from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **options):
        user = User(name='John', email='john@mail.ru', password='secret', age=25)

        user.save()
        self.stdout.write(f'{user}')
