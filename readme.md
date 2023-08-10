# Для запуска под Linux Ubuntu
## Создайм виртуальное окружение и устанавливаем зависимости 

###### python3 -m venv env
###### source env/bin/activate
###### pip install -r requirements.txt

## Создаём базу данных postgresql и пользователя с привелегиями
###### sudo -u postgres psql
###### CREATE DATABASE calldb;
###### CREATE USER calluser WITH ENCRYPTED PASSWORD '12345test
###### ALTER ROLE myuser SET client_encoding TO 'utf8';
###### ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
###### ALTER ROLE myuser SET timezone TO 'UTC';
###### GRANT ALL PRIVILEGES ON DATABASE calldb TO calluser;

## Создаём и применяем миграции
###### python manage.py makemigrations
###### python manage.py migrate

## Запускаем тесты
###### ./manage.py test
