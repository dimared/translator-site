# Сайт - нейросетевой переводчик

Сервис состоит из двух частей, сообщающихся по протоколу gRPC (описание доступных полей находится в файле [proto/translator.proto](proto/translator.proto)):

1. [Translator](translator/translator.py) - бэкенд, использующий [генеративные модели](translator/models.py) для перевода с русского на английский язык. Для запущенного сервиса доступны некоторые [тесты](translator/test_server.py).

2. [Site](site/__main____.py) - фронтенд на Flask, который обращается к бэкенду-переводчику. 


## Запуск
### Docker
Сперва создаем сеть:
```
docker network create microservices
```

Запуск бэкенда:
```
docker build . -f translator/Dockerfile -t translator

sudo docker run -p 50051:50051 --network microservices --name translator translator
```

Запуск Flask-приложения:
```
docker build . -f site/Dockerfile -t site 

docker run -p 0.0.0.0:5000:5000/tcp --network microservices -e TRANSLATOR_HOST=translator --name site site
```

### Docker-compose
(!) Еще не реализован


## Frontend:
[Flask 2.0](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

[Bootstrap theme](https://bootswatch.com/cyborg/)


## Backend:
[Huggingface model](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en)


## TODO:
* Запуск через `docker-compose up`
* Обработка ошибок
* Health probe бэкенда отражать на сайте
* Не очищать введенный текст
* Прокидывать seed для перевода, фиксировать в тестах
* Поддержать другие языки (не только перевод с русского на английский)
* Тесты и деплой через Gitlab CI / Github Actions
