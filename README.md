# Perfin: A personal finance app made with Django

This is a side project I built to sharpen my Django skills and also help me with my finances since I got sick of doing everything
on a spreadsheet.

This project utilizes many things that are important when making a web app using Django:

- Models, Fields and Queries (ORM)
- Forms
- Views and Generics
- Authentication and admin
- Templates and tags
- Fixtures
- Static (CSS & Javascript)
- Validators and utils

#### TODO

- REST API
- User-level permissions


## Get Started

Git clone the project.

```
git clone https://github.com/mredaoudi/perfin
```

Go inside the project, create a virtual environment and install the requirements


```
cd perfin
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the migrations, load the categories fixtures and start the application

```
python manage.py migrate
python loaddata categories
python manage.py runserver
```

For now, you can only view the landing page. To be able to use the application you need to have a user account which you can create in two ways:

- Django shell
- Admin panel

```
# OPTION 1
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(username='...', email='...', password='...')

# OPTION 2
# After completing command below, go to localhost:8000/admin and create user there
python manage.py createsuperuser
```


