# Django - No such table: main.auth_user__old
# ANSWER
# For me I first used: pip install --upgrade django==2.1.5 Then I used python manage.py makemigrations and then python manage.py migrate Then I used python manage.py runserver Worked like a charm, I didn't have to delete db!
