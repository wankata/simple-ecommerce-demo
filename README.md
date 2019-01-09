simple-ecommerce-demo
=====================

Simple e-commerce demo project written on Python with Django and MySQL

Prerequisites
------------------------------

You need to have [Git](https://git-scm.com/), [Docker CE](https://docs.docker.com/install/ "Install Docker CE") and [Docker
Compose](https://docs.docker.com/compose/install/ "Install Docker Compose") installed.

In the following examples, I assume, that your docker environment needs root privilegues to work properly. If it doesn't
just remove the *'sudo'* infront of the commands. If your environment is other than GNU/Linux, there may be some
differences in the interaction with Docker, so please follow the [Docker documentation](https://docs.docker.com/) if
something doesn't suits you.

Installation and configuration
------------------------------

First of all you need to clone the repository and initialize it's submodules:

    $ git clone --recurse-submodules https://github.com/wankata/simple-ecommerce-demo.git

If you already have cloned the repo without --recurse-submodules, you need to:

    $ git submodule init
    $ git submodule update

Then you need to setup your environment properly. Copy the **db.env.tmpl** and **web.env.tmpl** files in **db.env** and
**web.env** and edit them corresponding to your environment. These files contain sensitive data such as passwords and
secret keys, so you want to keep them secret. But don't worry, the **.env* files are listed in the *.gitignore*.

Now you are ready to start the docker environment. At the first run, it will last a little bit longer, because of the
initial image setup.

    $ sudo docker-compose up

When the environment is up and running, log in on the web server and run the migrations needed:

    $ sudo docker-compose exec web bash
    # ./manage.py migrate

or execute it directly:

    $ sudo docker-compose exec web ./manage.py migrate

Now you are ready to add a superuser account:

    $ sudo docker-compose exec web ./manage.py createsuperuser

And you are ready! Log into the [Django admin](http://127.0.0.1:8000/admin/) and be yourself!

Django settings
---------------

In the settings package, you will find:
  * **base.py**
  It includes all Django settings, that are environment agnostic.
  * **development.py**
  It includes specific settings, used in your development environment.
  * **production.py**
  It includes specific settings, used in production.
  
Be careful not to put sensitive data directly in the setting files. Use the environment variables for this!
You should use the **get_env_variable()** utility method for this, just like:

    SECRET_KEY = get_env_variable('SECRET_KEY')

**NB!:** Don't forget to put the newly added environment variables in the .tmpl files.

Known issues
------------
  * ecommerce.wsgi is not properly configured. If you want to run django in production with wsgi, you need to set the
    correct DJANGO_SETTINGS_MODULE
