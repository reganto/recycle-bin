# Recycle Bin

- Soft delete articles with Django
- Celery Beat periodic task to permanently remove articles that have been deleted for 30 days.

## Design Document

[Recycle Bin Design Document](https://murtaza.blog.ir/post/Recycle-Bin-Design-Document)

## Tools

- Django as web framework

- Celery as distributed task queue

- RabbitMQ as message queue (Celery broker)

- Redis as Celery result backend

- PostgreSQL as DBMS

- Nginx as reverse proxy (it serves static files also)

- PostgreSQL as DBMS

- Docker as contianer manager


## Run

```bash
docker compose -f docker-compose.prod.yml up
```

## How it works

![recycle-bin](https://user-images.githubusercontent.com/29402115/199185546-ecbbb892-ba8a-4865-aff6-d2f49d7ef496.gif)

## Open your mailbox and 
tell.reganto[at]gamil.com

Hello!
