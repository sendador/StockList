from django.test import TestCase
from stock.models import StockList


class TestModelsStr(TestCase):
    def setUp(self):
        self.stock = StockList.objects.create(
            company_name='ZYWIEC',
            company_code='ZYW',
            stock_price='10',
        )

    def tearDown(self):
        self.stock.delete()

    def test__str__(self):
        self.assertEqual(str(self.stock), self.stock.company_name)
