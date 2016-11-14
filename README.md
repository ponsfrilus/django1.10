From trydjango1.10 https://www.youtube.com/playlist?list=PLEsfXFp6DpzQSEMN5PXvEWuD2gEWVngCZ


## New project creation and basic commands

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


## Django shell

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


## Django Model manager

~~~ bash
python manage.py shell
~~~

~~~ python
In [1]: from shortener.models import ShortURL

In [2]: ShortURL.objects.all().count()
Out[2]: 4

In [3]: ShortURL.objects.count()
Out[3]: 5

In [4]: for u in ShortURL.objects.filter(id__gte=1): print(u.shortcode)
12EZ4I
home
google
bb
k5mdcx

In [5]: ShortURL.objects.regenerate_all_shortcodes()

In [6]: for u in ShortURL.objects.filter(id__gte=1): print(u.shortcode)
w7wfb8
2omn03
wkkypy
4ej8uj
x0grn0
~~~


## Custom Django Management commands

~~~ bash
python manage.py dumpurls
~~~

~~~ out
zts5ze -> http://enacit.epfl.ch
age9m9 -> http://www.epfl.ch
u66ec3 -> http://www.google.com
l6zou4 -> http://example.com
~~~

~~~ bash
python manage.py refreshcodes
python manage.py dumpurls
~~~

~~~ out
7k95wc -> http://enacit.epfl.ch
axdpd2 -> http://www.epfl.ch
n17jsw -> http://www.google.com
bbqfwq -> http://example.com
~~~


## Basic views

http://127.0.0.1:8000/
http://127.0.0.1:8000/view-1/
http://127.0.0.1:8000/view-2/


## Start to decode URLs

http://127.0.0.1:8000/a/Alice/
http://127.0.0.1:8000/b/Bob/


## host management

http://django-hosts.readthedocs.io/en/latest/

~~~ snip /etc/hosts
127.0.0.1       shortme.com www.shortme.com blog.shortme.com
~~~

~~~ bash
pip install django-hosts
~~~

http://blog.shortme.com:8000/a/axdpd2/


## Forms and Fields validation

~~~ bash
python manage.py makemigrations
python manage.py migrate
~~~

Test on
+ http://www.shortme.com:8000/
+ http://www.shortme.com:8000/admin/
