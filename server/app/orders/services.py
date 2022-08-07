import csv
from dataclasses import dataclass
from datetime import date

from django.conf import settings

from app.google.services import GoogleDriveService
from app.orders.models import Order as OrderModel


@dataclass
class Order:
    id: int
    number: int
    price: int
    delivery_date: date


class OrderService:
    def __init__(self):
        self.service = GoogleDriveService()

    def parse_orders(self, file_id: str) -> list[Order]:
        """
        Parse orders from Google Drive

        :return: Orders list (id, order number, price, delivery_date)
        """
        data = self.service.get_file_data(file_id)
        result = []
        for row in csv.reader(data.split('\n'), delimiter=','):
            result.append(Order(int(row[0]), int(row[1]), int(row[2]), date(row[3])))
        return list(csv.reader(data.split('\n'), delimiter=','))

    def update_orders(self, file_id: str = None):
        """ Gets Orders from specified file in Google Drive and update data in Database """

        file_id = file_id or settings.GOOGLE_DRIVE_ORDERS_FILE_ID

        orders = self.parse_orders(file_id)

        for order in orders:
            OrderModel.objects.update_or_create(
                id=order.id,
                defaults=dict(
                    price_in_usd=order.price,
                    price_in_rub=order.price * 60,
                    number=order.number,
                    delivery_date=order.delivery_date
                )
            )


