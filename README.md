From trydjango1.10 https://www.youtube.com/playlist?list=PLEsfXFp6DpzQSEMN5PXvEWuD2gEWVngCZ


~~~ bash
mkdir django1.10
cd django1.10/

virtualenv py3 -p python3
. py3/bin/activate
pip install django==1.10.3

django-admin.py startproject shortme
cd shortme
python manage.py startapp shortener

python manage.py migrate
python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate

python manage.py migrate shortener --fake
~~~

~~~ bash
python manage.py shell
~~~

~~~ python
from shortener.models import ShortURL

ShortURL.objects.all()

url1 = ShortURL.objects.create()
url1.url = "http://www.epfl.ch"
url1.shortcode = "home"
url1.save()

url2, created = ShortURL.objects.get_or_create(url="http://www.epfl.ch")
created
url2.shortcode

url3 = ShortURL.objects.get(url="www.google.com")
ShortURL.objects.get_or_create(url="http://www.google.com", shortcode="google")
ShortURL.objects.get_or_create(url="http://www.google.com", shortcode="google")
~~~

https://docs.djangoproject.com/en/1.10/howto/writing-migrations/#migrations-that-add-unique-fields

~~~ bash
rm -rf shortener/migrations/*
rm db.sqlite3
python manage.py makemigrations shortener
python manage.py createsuperuser

~~~
