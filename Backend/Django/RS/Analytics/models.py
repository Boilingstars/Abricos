from django.db import models

class GoodsMarketAnalysis(models.Model):

    class Meta:
        app_label = 'Analytics'

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

new_analytics = BuisnessMarketAnalysis(market_volume=800, found_enemies=23, market_concentration=20, market_potential=1, available_market=1.4, demand_growth=0.5, purchasing_power=90, customer_preferences=8090, market_penetration_rate=2)