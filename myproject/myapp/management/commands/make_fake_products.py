import random
from random import uniform

from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Колличество продуктов для генерации")

    def handle(self, *args, **options):
        products = []
        count = options.get('count')
        for i in range(1, count):
            products.append(Product(
                name=f'Продукт номер {i}',
                price=uniform(0.01, 999_999.99),
                description=f'Описаник которое никто не читает',
                quantity=random.randint(1, 10_000),
            ))
        Product.objects.bulk_create(products)
        self.stdout.write(f'Созданно {count} фейковых продуктов')
