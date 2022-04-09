# Storage Security Panel

This web application implements a security panel, that can be used to watch over passcard access to the storage facility.
Current version allows:
- Listing of all active passcards
- Listing of all passcard holders currently on storage visit
- Listing of all visits (past and present) for any active passcard holder.
- Simple duration check to highlight suspiciously long storage visits (both past and present)

### Installation guidelines

You must have Python3 installed on your system.
You may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.
```
pip install -r requirements.txt
```
It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

This application is based on [Django web-framework](https://www.djangoproject.com/). All Django related settings can be found in `./project/settings.py`. Avoid making any changes to default configuration, if you are not sure what you are doing.

All project specific settings are stored in `.env` file in root folder. Do not forget to create one!

Below you can find what variables are expected in your `.env` file:

```
DB_HOST = ''
DB_PORT = 0
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''

SECRET_KEY = ''
ALLOWED_HOSTS = ''

DEBUG = false
```

`DB_HOST` is the host address of the PostgreSQL server.

`DB_PORT` is the TCP port the PostgreSQL server listens on.

`DB_NAME` is the name of the database.

`DB_USER` and `DB_PASSWORD` refers to respective credentials to access the database.

`SECRET_KEY` is special unique string, usually set to something unpredictable. As name implies - keep it secret. Find more about secret key [here](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key).

`ALLOWED_HOSTS` is a list of domain names/masks expected to be served by server. This value must be set up to prevent [HTTP Host header attacks](https://docs.djangoproject.com/en/3.2/topics/security/#host-headers-virtual-hosting). Find more about allowed hosts [here](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts)

`DEBUG` is boolean flag, that controls wether your Django application runs in debug mode. That might be useful in development, but deploying your app with debug mode switched on is a **BAD IDEA**. Find more about debug mode [here](https://docs.djangoproject.com/en/3.2/ref/settings/#debug). `DEBUG` variable is optional and default value is set to `False`

### Basic usage

You can start your web application by simple command:

```
py manage.py runserver
```

This will run your webapp on local lightweight web server. Default address is `127.0.0.1:8000`

You can explicitly specify IP address and port by passing an argument:
```
py manage.py runserver 1.2.3.4:8080
```

You can check other avaliable options for the `runserver` command over [here](https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver).

### Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.