from django.core.management.base import BaseCommand
from stock.models import StockList
from bs4 import BeautifulSoup
import requests
from decimal import Decimal


class Command(BaseCommand):
    help = 'Download current stock prices and names'

    def handle(self, *args, **options):
        r = requests.get('https://www.bankier.pl/gielda/notowania/akcje')
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, 'html.parser')
        stock_table = soup.find('table', 'sortTable',
                                'floatingHeaderTable').tbody
        stock_table.find('tr', 'adv').decompose()
        for sibling in stock_table.tr.next_siblings:
            #Uniknięcie znaków specjalnych jak np. \n
            if len(str(sibling)) == 1:
                continue
            StockList.objects.update_or_create(
                company_code=sibling.find('td', 'colWalor').find('a').text,
                defaults={
                    'company_name': sibling.find('td', 'colWalor').find('a')['title'],
                    'stock_price': Decimal(sibling.find('td', 'colKurs').text.replace(',', '.').replace('\xa0', ''))
                }
            )
        self.stdout.write("Stock list updated success")
