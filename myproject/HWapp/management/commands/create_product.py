from django.core.management.base import BaseCommand
from HWapp.models import Client, Product


class Command(BaseCommand):
    help = 'create product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='NAME')
        parser.add_argument('description', type=str, help='DESCRIPTION')
        parser.add_argument('price', type=int, help='PRICE')
        parser.add_argument('count', type=int, help='COUNT')

    def handle(self, *args, **options):
        product = Product(name=options.get('name'), description=options.get('description'),
                          price=options.get('price'), count=options.get('count'))

        product.save()
        self.stdout.write(f'{product}')
