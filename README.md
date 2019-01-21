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

Then you need to setup your environment properly. Copy the **./environment/db.env.tmpl** and **./environment/web.env.tmpl** files in **./environment/db.env** and
**./environment/web.env** and edit them corresponding to your environment. These files contain sensitive data such as passwords and
secret keys, so you want to keep them secret. But don't worry, the **.env* files are listed in the *.gitignore*.

Now you are ready to start the docker environment. At the first run, it will last a little bit longer, because of the
initial image setup.

    $ cd ./environment/
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

About code style
----------------

We use flake8 with default configuration for code checks.

If you want to exclude some code from the checs, because they are not appropriate, you should consider the following
conventions:
  * Exclude code only when it is really OK and it won't be fixed
  * Exclude only specific codes and not all checks, e.g.:

        # noqa: E501

Catalogue app
----------------

The Catalogue app exposes a category tree and the related to them products. It makes use of
[django-mptt](https://github.com/django-mptt/django-mptt) for the category tree,
[django-money](https://github.com/django-money/django-money) for the product's price,
[easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) for the product's image and
[django-bootstrap4](https://github.com/zostera/django-bootstrap4) for the layout.

If you need the category menu outside the Catalogue app, take a look at the *menu block* inside the base.html. You will
need the small script inside the *extra_body block*, related to that menu, too.

If you want to change the look and feel of the catalogue, feel free to override it's default templates inside your
project's template dir.

The Catalogue app is a simple brochure. If you need it to be a part of an online store, you may want to integrate it
with your basket. The *category_detail.html* provides you with a *basket block* for that purpose. You need to extend the
template, override the basket block and you are ready! All other styles will remain as by default.

Known issues
------------
  * ecommerce.wsgi is not properly configured. If you want to run django in production with wsgi, you need to set the
    correct DJANGO_SETTINGS_MODULE
  * There is no clearsessions cron job for clearing expired sessions in the backend. Implement this in production to
    prevent unmanaged db growth.
  * Make sure to change SESSION_COOKIE_SECURE to true when https is implemented.
  * To make the Catalogue app really reusable, we need to write in-app documentation about the configuration it needs
    and define it's dependencies. Basicly to explain how to work with django-money, currencies and exchange rates.
  * Currently we allow only BGN currency to be used. If we want to have a multy currency site, we need to make use of
    djmoney.contrib.exchange and to extend our apps to use it properly.
  * Django-money doesn't represent the BGN really right. I am not really convinced that it is the best choice for
    working with money.
  * We probably want to have an in-app settings to preconfigure things like THUMBNAIL_ALIASES suitable for the default
    app templates.
  * The templates are not really responsive. We use the same column count nevertheless the device width.
  * When you have less items on a row, the card width increases.
  * All strings are marked as translatable, but no real localisation is implemented yet.
