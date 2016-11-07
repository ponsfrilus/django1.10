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
~~~
