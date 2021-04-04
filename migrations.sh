echo "*************** Running migrations $APP **************"
cd django_rest_api

python manage.py makemigrations $APP
echo "*************** Migrations ran $APP *******************"
