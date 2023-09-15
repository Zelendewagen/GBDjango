from django.core.management.base import BaseCommand
from HWapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "delete client from id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="User ID")

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()

        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')
