# Тестовое задание Python Backend

## Масалов Тихон

## Описание проекта
Данный проект представляет собой REST API для получения информации о городах, улицах и магазинах.

Приложение и база данных (PostgreSQL) запускаются в Docker контейнере      


### API Docs:
- `/city/` (GET) - получение списка всех городов в базе данных
    - Пример запроса: `GET /city/`
    - Пример ответа:
        ```
        [
            {
                "id": 1,
                "city_name": "Казань",
            },
            {
                "id": 2,
                "city_name": "Москва",
            }
        ]
        ```
- `/city/<city_id>/street` (GET) - получение списка всех улиц в заданном городе
    - Пример запроса: `GET /city/1/street`
      - Пример ответа:
          ```
          [
              {
                  "id": 1,
                  "street_name": "Ленина",
                  "city": {
                     "id": 1,
                     "city_name": "Казань"
                  }
              },
              {
                  "id": 2,
                  "street_name": "Пушкина",
                  "city": {
                     "id": 1,
                     "city_name": "Казань"
                  }
              },
          ]
          ```
- `/shop/?street=&city=&open=0/1 ` (GET) - получение списка всех магазинов в базе данных, с возможностью фильтрации по городу, улице и наличию открытых магазинов в данный момент
    - Пример запроса: `GET /shop/?street=Пушкина&city=Казань&open=1`
    - Параметры запроса:
        - `street` - название улицы
        - `city` - название города
        - `open` - фильтрация по открытым магазинам. Если `0`, то вернуть магазины, которые закрыты в данный момент, если `1`, то вернуть только открытые.
    - Пример ответа:
         ```
          [
          {
              "id": 2,
              "shop_name": "Продукты",
              "city": {
                  "id": 1,
                  "city_name": "Казань"
              },
              "street": {
                  "id": 2,
                  "street_name": "Пушкина",
                  "city": {
                      "id": 1,
                      "city_name": "Казань"
                  }
              },
              "house": "2",
              "opening_time": "06:00:00",
              "closing_time": "20:00:00"
          }
      ]
      ```

- `/shop/` (POST)  - добавление нового магазина в базу данных
- Content-Type: application/json

    - Пример запроса:
        ```
         {
            "shop_name": "Магазин Хороших Продуктов",
            "city": {
                "city_name": "Казань"
            },
            "street": {
                "street_name": "Пушкина",
                "city": {
                    "city_name": "Казань"
                }
            },
            "house": "5",
            "opening_time": "07:00:00",
            "closing_time": "21:00:00"
        }
        ```
    - Параметры запроса:
        - `shop_name` - название магазина
        - `city_name` - название города
        - `street_name` - название улицы
        - `house` - номер дома
        - `opening_time` - время открытия в формате `HH:MM:SS`
        - `closing_time` - время закрытия в формате `HH:MM:SS`
    - Пример ответа (JSON с id созданного магазина):
        ```
        {
            "id": 9
        }
        ```
               
## Подготовительные действия

Для успешной работы проекта необходимо выполнить следующие шаги:

1. Установить Docker на свой компьютер, если он еще не установлен.(https://www.docker.com/get-started)

2. Склонировать данный репозиторий на свой компьютер (`git clone https://github.com/T-MA-S/TestAPI.git`)

3. Перейти в директорию с проектом (`cd TestAPI`)

4. Запустить Docker контейнер с помощью команды `docker-compose up`


## Информация о доступах

Для доступа к Admin панели необходимо использовать следующие параметры:

- Login : admin
- Email : test@test.com
- Password : 1

При создании учетной записи superuser'a будет создан тестовый набор данных
## Описание, как запустить проект

После выполнения подготовительных действий проект будет доступен по адресу `http://localhost:8000/`. 

Для тестирования API можно воспользоваться любым endpoint'ом, указанным в документации