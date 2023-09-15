from django.core.management.base import BaseCommand
from HWapp.models import Order


class Command(BaseCommand):
    help = "delete order from id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="ID")

    def handle(self, *args, **options):
        pk = options.get('pk')
        order = Order.objects.filter(pk=pk).first()

        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')
