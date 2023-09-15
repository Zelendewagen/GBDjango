from django.core.management.base import BaseCommand
from HWapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "create order"

    def add_arguments(self, parser):
        parser.add_argument('clientID', type=int, help='ID')
        parser.add_argument('productID', type=int, help='ID')

    def handle(self, *args, **options):
        client = Client.objects.get(pk=options.get('clientID'))
        product = Product.objects.get(pk=options.get('productID'))
        order = Order(client=client, total_price=0)
        order.save()
        order.products.add(product)
        order.total_price += product.price
        order.save()

        self.stdout.write(f'{order}')
