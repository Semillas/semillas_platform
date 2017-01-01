# semillas_backend
================

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
![MIT License](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)
[![Travis-CI](https://travis-ci.org/Semillas/semillas_backend.svg?branch=master)](https://travis-ci.org/Semillas/semillas_backend)
[![Coverage Codecov](https://codecov.io/gh/Semillas/semillas_backend/branch/master/graph/badge.svg)](https://codecov.io/gh/Semillas/semillas_backend)
[![Updates](https://pyup.io/repos/github/semillas/semillas_backend/shield.svg)](https://pyup.io/repos/github/semillas/semillas_backend/)



## Social Currency


It is a transparent, nonprofit platform for the exchange of goods and services in which participation don't require legal tender involvement.

It is based on the abundancy of resources, in the creative, artistic, manual and intelectual capacity of members. They could be children, elder people, teenagers, workers, housewives, unemployed, etc.

We are a community of developers willing to learn. Join us and we will give you fully support.

* **Website:** https://www.semillasocial.org
* **API Rest Endpoints:** https://www.semillasocial.org/docs (You should be registered and signed-in)
* **React App**: **https://www.semillasocial.org/webapp** is the ReactJS being executed.
* **Write us**: info.semillasocial@gmail.com


## Apps Distribution
In Django the term application describes a Python package that provides some
set of features. Applications may be reused in various projects.

We have the following main ones:
* **services**: It contains a basic Service entity: Some service being offered or for sale.
* **semillas_backend/users**: The User's models and views
* **landing**: Visible landing website. No logic. No models.
* **webapp**: ReactJS - Redux Web client consuming from the [API](https://www.semillasocial.org/docs/).
* **swagger**: Preview for every API endpoint. Check it here:  [API](https://www.semillasocial.org/docs/)
* **wallet**: App responsible of user wallet and movements



## Setting Up Your Development environment with Docker Compose

#### Linux

* Install Docker Engine:
  For example, in Ubuntu I installed it following this:
  https://docs.docker.com/engine/installation/linux/ubuntulinux/

#### Mac
  Docker is native in Mac now. Drag and drop and enjoy.

### Start Everything
Once docker compose is installed and running:

```$ sudo docker-compose -f dev.yml up```


## Basic Commands

### Run the migrations pending
Migrations are handled by Django. If you just set up your development environment
probably there is a lot of migrations you have to run in your database so is in
concordance with the models defined in the code.

* See all migrations and which one is left to apply.

 ```$ docker-compose -f dev.yml run django python manage.py showmigrations```
* Run all migrations with this command:

 ```$ docker-compose -f dev.yml run django python manage.py migrate```

Any change in any model can incur in a database migration. Check them here:
https://docs.djangoproject.com/en/1.10/topics/migrations/

### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

 ```$ docker-compose -f dev.yml run django python manage.py createsuperuser```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Test coverage
To run the tests, check your test coverage, and generate an HTML coverage report::

````
$ docker-compose -f dev.yml run django coverage run manage.py test
$ docker-compose -f dev.yml run django coverage html
$ open htmlcov/index.html
```
### Running tests with py.test

```$ docker-compose -f dev.yml run django py.test```


### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server MailHog with a web interface is available as docker container.

Mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to http://127.0.0.1:8025


### Error Log: Sentry

https://sentry.io/semillas



### Deployment

Whenever master branch is updated with a new commit or merge. A deploy will be triggered.
Check it on https://www.semillasocial.org

Whatever is pushed to 'dev' branch it will automatically be deployed to http://alpha.semillasocial.org
