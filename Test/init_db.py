from django.contrib.auth import get_user_model
from shops.models import City, Street, Shop
import datetime


def create_super_admin():
    User = get_user_model()
    if not User.objects.filter(email='test@test.com').exists():
        admin = User.objects.create_superuser('admin', 'test@test.com', '1')
        # fill table with test data
        create_test_data()


def create_test_data():
    cities_list = [
        City(city_name='Казань'),
        City(city_name='Москва'),
        City(city_name='Ульяновск'),
        City(city_name='Новосибирск'),
        City(city_name='Нижний Новгород'),
    ]

    City.objects.bulk_create(cities_list)

    streets_list = [
        Street(street_name='Ленина', city=cities_list[0]),
        Street(street_name='Пушкина', city=cities_list[0]),
        Street(street_name='Фролова', city=cities_list[1]),
        Street(street_name='Победы', city=cities_list[1]),
        Street(street_name='Ивановская', city=cities_list[1]),
        Street(street_name='Братьев Карамазовых', city=cities_list[2]),
        Street(street_name='Тестовая #47', city=cities_list[3]),
        Street(street_name='Последняя', city=cities_list[4]),
    ]

    Street.objects.bulk_create(streets_list)

    shops_list = [
        Shop(shop_name='Магазин', street=streets_list[0], city=cities_list[0], house='34',
             opening_time=datetime.time(8, 0),
             closing_time=datetime.time(23, 0)),
        Shop(shop_name='Продукты', street=streets_list[1], city=cities_list[0], house='2',
             opening_time=datetime.time(6, 0),
             closing_time=datetime.time(20, 0)),
        Shop(shop_name='Домашний', street=streets_list[2], city=cities_list[1], house='9',
             opening_time=datetime.time(19, 0),
             closing_time=datetime.time(23, 0)),
        Shop(shop_name='Супермаркет', street=streets_list[3], city=cities_list[1], house='1714А',
             opening_time=datetime.time(1, 0),
             closing_time=datetime.time(12, 0)),
        Shop(shop_name='Минимаркет', street=streets_list[4], city=cities_list[1], house='68Б',
             opening_time=datetime.time(5, 0),
             closing_time=datetime.time(9, 0)),
        Shop(shop_name='Алкомаркет', street=streets_list[5], city=cities_list[2], house='654',
             opening_time=datetime.time(5, 0),
             closing_time=datetime.time(22, 0)),
        Shop(shop_name='Фрукты и Овощи', street=streets_list[6], city=cities_list[3], house='12',
             opening_time=datetime.time(6, 0),
             closing_time=datetime.time(17, 0)),
        Shop(shop_name='Мясной', street=streets_list[7], city=cities_list[4], house='57',
             opening_time=datetime.time(0, 0),
             closing_time=datetime.time(18, 0)),
    ]

    Shop.objects.bulk_create(shops_list)
