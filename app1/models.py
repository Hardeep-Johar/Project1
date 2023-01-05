from django.db import models

# Create your models here.
class Holding(models.Model):
    iso = models.CharField(max_length=3)
    local_currency_value = models.FloatField(default=0.0)
    buy_date = models.DateField()
