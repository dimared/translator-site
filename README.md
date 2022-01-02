# Сайт - нейросетевой переводчик

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
* Поддержать другие языки (не только перевод с русского на английский)
* Тесты и деплой через Gitlab CI / Github Actions

