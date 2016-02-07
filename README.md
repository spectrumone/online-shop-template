# online-shop-template
A comprehensive online shop template to cover most online shop features.

###Current Features
* Product Catalog
* Shopping cart using django sessions
* Customer orders management
* Asynchronous notifications to cutomers using Celery

###Installation
1. `pip install -r requirements.txt`
2. install rabbitmq from the <b>RabbitMQ</b> site.
3. check if rabbitmq-server is installed by running: `sudo service rabbitmq-server status`

###Usage
1. run <b>Celery</b>: `celery -A myshop worker -l info` (captures the terminal)
2. start test db: `python manage.py syncdb`
3. create migrations if ever there are any: `python manage.py makemigrations`
4. run migrations: `python manage.py migrate`
5. run online shop locally: `python manage.py runserver` (captures the terminal)

###Monitor Async Tasks
1. run flower on a separate terminal: `celery -A myshop flower` (captures the terminal)

###To Do
1. Integrate a payment gateway
2. Manage payment notifications
3. Export orders to CSV files
4. Generate PDF invoices dynamically
5. Create coupon system to apply discounts
6. Adding internationalization to online shop
7. Use <b>Rosetta</b> to manage translations
8. Translating modles using <b>django-parler</b>
9. Build product recommendation engine
10. Refactor app to use class based views instead
11. Refactor for best practices
