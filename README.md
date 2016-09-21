# semillas_backend
================

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000

.. image:: https://travis-ci.org/Semillas/semillas_backend.svg?branch=master
    :target: https://travis-ci.org/Semillas/semillas_backend

.. image:: https://codecov.io/gh/Semillas/semillas_backend/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Semillas/semillas_backend


## Social Curency


It is a transparent, nonprofit platform for the exchange of goods and services in which participation don't require legal tender involvement.

It is based on the abundancy of resources, in the creative, artistic, manual and intelectual capacity of members. They could be children, elder people, teenagers, workers, housewives, unemployed, etc.


* **Website:** https://www.semillasocial.org
* **API Rest Endpoints:** https://www.semillasocial.org/docs (You should be registered and signed-in)
* On the url **https://www.semillasocial.org/webapp** is the ReactJS being executed.


## Apps Distribution
In Django the term application describes a Python package that provides some
set of features. Applications may be reused in various projects.

We have the following main ones:
* **board**: It contains a basic Service entity: Some service being offered or for sale.
* **semillas_backend/users**: The User's models and views
* **landing**: Visible landing website. No logic. No models.
* **webapp**: ReactJS - Redux Web client consuming from the [API](https://www.semillasocial.org/docs/).


## Setting Up Your Development environment with Docker Compose

#### Working on Ubuntu

* Install Docker Engine:
  For example, in Ubuntu I installed it following this:
  https://docs.docker.com/engine/installation/linux/ubuntulinux/

* Install Docker Compose:
  Using this instructions for Ubuntu:
  https://docs.docker.com/compose/install/

* Once docker compose is installed and docker engine service is running:
    $ sudo docker-compose -f dev.yml up



#### Alternative way of installing Docker Compose:

    $ curl -sSL https://get.docker.com
    $ pip install docker-compose  # run it as sudo to install it globally.
    $ gpasswd -a $USER docker  # add user to docker group
    # login/logout from shell


## Basic Commands

### Run the migrations pending
Migrations are handled by Django. If you just set up your development environment
probably there is a lot of migrations you have to run in your database so is in
concordance with the models defined in the code.

* See all migrations and which one is left to apply.
      docker-compose -f dev.yml run django python manage.py showmigrations
* Run all migrations with this command:
      docker-compose -f dev.yml run django python manage.py migrate

Any change in any model can incur in a database migration. Check them here:
https://docs.djangoproject.com/en/1.10/topics/migrations/

### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ docker-compose -f dev.yml run django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Test coverage


To run the tests, check your test coverage, and generate an HTML coverage report::


    $ docker-compose -f dev.yml run django coverage run manage.py test
    $ docker-compose -f dev.yml run django coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ docker-compose -f dev.yml run django py.test




### Live reloading and Sass CSS compilation

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html






### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

.. _mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``


### Error Log: Sentry

https://sentry.io/semillas



### Deployment

Whenever master branch is updated with a new commit or merge. A deploy will be triggered.
Check it on https://www.semillasocial.org

Whatever is pushed to 'dev' branch it will automatically be deployed to http://alpha.semillasocial.org
