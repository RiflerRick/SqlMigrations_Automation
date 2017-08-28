## Sql Migration Hook

#### Introduction

In Django (version 1.11), the command `python manage.py makemigrations <app name>` is used to make sql migrations for mysql. It is an extraordinary feature of Django where if any changes are detected in the files, those changes are automatically accounted for and a corresponding sqlmigration python file is created in the migrations directory. Now it is also possible to see these migrations in the form of sql statements. These statements are actually executed in order to create all the required tables or drop tables as necessary. The way this is done is by using the following command.

`python manage.py sqlmigrate <app name> <migration version>`

If we go inside the app folder we will find a folder called migrations that actually contain all the migrations that we have made. The files in the migrations folder generally starts with a number like **0001**, **0002** in a sequence. This number is actually the migration version. This migration version is provided into the python sqlmigrate command in order to generate the sql statements. 

#### Objecttive

In the production server it may be necessary to run sql statements separately. In order to achieve that all we would ideally need to do is to simply have one command and that command would validate for errors and generate all sql statements. This should ideally happen with just one command. Our objective therefore as simple as it may seem is simply to write a script t automate this task so that it can be done in just one command.

#### Requirements

Requirements are pretty much nothing. Right now this looks like another hook script that we have to build. Simply so that whenever the hook is triggered because of a push to the repo. The only catch this time is that we will be requiring the entire repo at the place where the script will run. Otherwise the concept of makemigrations won't even work. This would technically mean that the hook must be installed in the same place where the repo entirely is placed on production. 

Note: When using Django 1.11 the default database is always going to be sqlite however sqlite is a rather light database and for any big project the default choice of database would be mysql. In order to run mysql in Django we need to `pip install mysql-python`. 

There is a slight complication here, when a PR is sent(if we think of it from the PR point of view) the code is not pushed yet, so for us to be able to use django's makemigrations command we need to have the code pushed.

Here is the solution to this problem. Django Sql migrations is a super powerful tool. We can think of sql migrations as a VCS and moreover as long as you have a python module(a directory with a `__init__.py` file in it) inside your django project containing a models.py file and apps.py file containing a configuration class and also the directory name is listed in installed apps in `settings.py`, sql migrations is going to work in it. 

On the remote server (wherever the production code is placed)there can be a single script that will run, the script will do the following:

Simply run Sqlmigrations on the application and everything will start working fine.

