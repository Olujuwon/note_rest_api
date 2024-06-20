FROM python:3.9.19-alpine

RUN pip install django djangorestframework markdown django-filter django-cors-headers django-rest-knox

WORKDIR /app

COPY . .

RUN python manage.py test


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]