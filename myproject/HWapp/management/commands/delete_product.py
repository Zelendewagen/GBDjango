from django.core.management.base import BaseCommand
from HWapp.models import Product


class Command(BaseCommand):
    help = "delete client from id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="User ID")

    def handle(self, *args, **options):
        pk = options.get('pk')
        product = Product.objects.filter(pk=pk).first()

        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')
