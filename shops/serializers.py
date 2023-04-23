from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city_name')


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = ('id', 'street_name', 'city')


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()

    class Meta:
        model = Shop
        fields = ('id', 'shop_name', 'city', 'street', 'house', 'opening_time', 'closing_time')
