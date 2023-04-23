from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityListView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class StreetListView(APIView):
    def get(self, request, city_id):
        streets = Street.objects.filter(city_id=city_id)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopListView(APIView):
    def get_filtered_queryset(self, request):
        street_name = request.GET.get("street")
        city_name = request.GET.get("city")
        open_now = request.GET.get("open")

        query = Q()
        if street_name:
            query &= Q(street__street_name=street_name)
        if city_name:
            query &= Q(street__city__city_name=city_name)
        shops = Shop.objects.filter(query)

        if open_now is not None:
            now = timezone.now().time()
            if open_now == "0":
                shops = shops.exclude(opening_time__lte=now, closing_time__gte=now)
            else:
                shops = shops.filter(opening_time__lte=now, closing_time__gte=now)

        return shops

    def get_validated_nested_fileds(self, data):
        validated_data = data

        city_name = validated_data.get('city', {}).get('city_name')
        city = City.objects.get(city_name=city_name)

        validated_data['city'] = city

        street_name = validated_data.get('street', {}).get('street_name')
        street = Street.objects.get(city=city, street_name=street_name)

        validated_data['street'] = street
        return validated_data

    def get(self, request):
        shops = self.get_filtered_queryset(request)
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = self.get_validate_nested_fileds_data(serializer.validated_data)
            shop = Shop.objects.create(**validated_data)
            return JsonResponse({"id": shop.id}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
