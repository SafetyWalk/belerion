python manage.py makemigrations;
python manage.py migrate;
python manage.py loaddata initial_users_data.json;
python manage.py loaddata initial_manual_users_data.json;
python manage.py loaddata initial_google_users_data.json;
python manage.py runserver;