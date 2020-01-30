from django.db import models


class StockList(models.Model):

    company_name = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100, unique=True)
    stock_price = models.DecimalField(max_digits=20, decimal_places=4)
    runtime_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name
