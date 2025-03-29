from django.db import models

class GoodsMarketAnalysis(models.Model):

    class Meta:
        app_label = 'Analytics'

    product = models.CharField(max_length=100, default=None)
    market_volume = models.IntegerField()
    found_enemies = models.IntegerField()
    market_concentration = models.FloatField()
    market_potential = models.IntegerField()
    available_market = models.FloatField()
    demand_growth = models.FloatField()
    purchasing_power = models.FloatField()
    customer_preferences = models.IntegerField()
    market_penetration_rate = models.FloatField()

    def __str__(self):
        return f"Goods Market Analysis {self.id}"


class BuisnessMarketAnalysis(models.Model):
    
    class Meta:
        app_label = 'Analytics'

    project = models.CharField(max_length=100, default=None)
    market_volume = models.IntegerField()
    found_enemies = models.IntegerField()
    market_concentration = models.FloatField()
    market_potential = models.IntegerField()
    available_market = models.FloatField()
    demand_growth = models.FloatField()
    purchasing_power = models.FloatField()
    customer_preferences = models.IntegerField()
    market_penetration_rate = models.FloatField()

    def __str__(self):
        return f"Buisness Market Analysis {self.id}"
