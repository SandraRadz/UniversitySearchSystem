# University Search System

## How to run project

1. Create virtual environment 
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Commit DB migrations
```bash
python manage.py migrate
```
4. Create superuser to get access to admin site
```bash
python manage.py createsuperuser
```
5. Install and run Redis server
```bash
redis-server
```
6. Run Celery server
```bash
celery -A university_search_system worker -l info
celery -A university_search_system worker --pool=solo -l info 
```
7. Run the server
```bash
python manage.py runserver
```