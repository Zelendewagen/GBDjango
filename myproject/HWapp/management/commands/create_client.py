from django.core.management.base import BaseCommand
from HWapp.models import Client


class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="NAME")
        parser.add_argument('email', type=str, help="EMAIL")
        parser.add_argument('number', type=str, help="PHONE")
        parser.add_argument('address', type=str, help="ADDRESS")

    def handle(self, *args, **options):
        client = Client(name=options.get('name'), email=options.get('email'),
                        number=options.get('number'), address=options.get('address'))
        client.save()
        self.stdout.write(f'{client}')