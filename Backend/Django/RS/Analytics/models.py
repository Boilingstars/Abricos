from django.db import models

class GoodsMarketAnalysis(models.Model):

    class Meta:
        app_label = 'GoodsMarketAnalysis'

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
        app_label = 'BuisnessMarketAnalysis'

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

class Enemies(models.Model):
    license_key = models.CharField(max_length=40)

    class Meta:
        app_label = 'Users'

    def __str__(self):
        return self.username