from django.db import models

class Goods(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Планируемый'
        PUBLISHED = 1, 'Принятый'

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_category = models.CharField(max_length=100)
    markets = models.TextField()  # Хранение списка как текст
    date = models.DateTimeField(auto_now_add=True)  # Автоматически устанавливает дату создания
    published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)  # Автоматически устанавливает дату создания

    def __str__(self):
        return self.name