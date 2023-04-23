from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Street(models.Model):
    street_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"street {self.street_name} in {self.city}"

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    # ↓ не совсем понятно назначение этого поля, т.к. street уже несет в себе название города, но тз есть тз
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
