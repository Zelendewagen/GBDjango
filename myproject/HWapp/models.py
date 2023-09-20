from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    register = models.DateTimeField(auto_now=True)

    # objects = models.Manager()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, number: {self.number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    receiving = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images', default='default.png')

    # objects = models.Manager()

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, count: {self.count}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now=True)

    # objects = models.Manager()

    def __str__(self):
        return f'Client: {self.client.email}, total price: {self.total_price}, date: {self.date_order}'
