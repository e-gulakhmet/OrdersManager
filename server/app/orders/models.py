from django.db import models


class Order(models.Model):
    number = models.IntegerField('Order number')
    price_in_usd = models.IntegerField('Price in USD')
    price_in_rub = models.IntegerField('Price in RUB')

    delivery_date = models.DateField()

    def __str__(self):
        return f'Order {self.number}, {self.price}₽, {self.delivery_date}'
