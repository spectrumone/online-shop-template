# online-shop-template
A comprehensive online shop template to cover most online shop features.

###Notes
* Coded in python3

###Current Features
* Product Catalog
* Shopping cart using django sessions
* Customer orders management
* Asynchronous notifications to customers using Celery
* Integrate a payment gateway
* Manage payment notifications
* Export orders to CSV files
* Generate PDF invoices dynamically
* Automated PDF invoice sending after purchase
* Coupon System for providing discounts and promos

###Installation
1. To create a virtualenv for python3 (using vitualenvwrapper): `mkvirtualenv --python=/usr/bin/python3 <name of venv>`.
2. `pip install -r requirements.txt`
3. install rabbitmq from the <b>RabbitMQ</b> site.
4. check if rabbitmq-server is installed by running: `sudo service rabbitmq-server status`

###Usage
1. run <b>Celery</b>: `celery -A myshop worker -l info` (captures the terminal)
2. start test db: `python manage.py syncdb`
3. create migrations if ever there are any: `python manage.py makemigrations`
4. run migrations: `python manage.py migrate`
5. specify e-mail and password for automated e-mail sending (only configured for zohomail). `export EMAIL=<email> && export PASSWORD=<password>`
6. run online shop locally: `python manage.py runserver` (captures the terminal)

###Monitor Async Tasks
1. run flower on a separate terminal: `celery -A myshop flower` (captures the terminal)

###To Do
1. Adding internationalization to online shop
2. Build product recommendation engine
3. Automated Email sending should be at Celery
4. Add heartbeat and Dead Man's Snitch to Celery
5. Refactor app to use class based views instead
6. Refactor for best practices
