web: gunicorn school_Api.wsgi

release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput