from django.test import TestCase, Client
from django.urls import reverse
import requests
from io import StringIO
from django.core.management import call_command


class TestStockList(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)

    def test_sorting_ascending(self):
        response = self.client.get('/?sort=asc')
        self.assertEqual(response.status_code, 200)

    def test_sorting_descending(self):
        response = self.client.get('/?sort=desc')
        self.assertEqual(response.status_code, 200)

    def test_requests_connection(self):
        response = requests.get('https://www.bankier.pl/gielda/notowania/akcje')
        self.assertEqual(response.status_code, 200)

    def test_command_output(self):
        out = StringIO()
        call_command('stocklist', stdout=out)
        self.assertIn('Stock list updated success', out.getvalue())