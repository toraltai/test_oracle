# Для запуска через Docker:
    1. клоним проект
    2. docker compose build
    3. docker compose up
        После успешного контейнера нужно остановить контейнер, чтобы сделать миграции.
    4. docker compose run --rm web-app sh -c "python3 manage.py migrate"
    5. docker compose up.

# Для локального запуска:
    1. создаем виртуальное окружение:
        python3 -m venv venv

    2. устанавливаем все зависимости с текстовика req.txt
        pip install -r req.txt

    3. создаем файл .env и дописываем настройки:
        DB_NAME='db_name'
        DB_USER='db_user'
        DB_PASS='db_pass'
        DB_HOST='db_host'

    4. проводим миграции:
        python3 manage.py migrate

    5. создаем Супер пользователя:
        python3 manage.py createsuperuser
            в поле Phone number, прописываем admin
            следующие два инпута будет вами указанный пароль для входа в админку
    
    6. Запуск!
        python3 manage.py runserver