## Sql Migration Hook

#### Introduction

In Django (version 1.11), the command `python manage.py makemigrations <app name>` is used to make sql migrations for mysql. It is an extraordinary feature of Django where if any changes are detected in the files, those changes are automatically accounted for and a corresponding sqlmigration python file is created in the migrations directory. Now it is also possible to see these migrations in the form of sql statements. These statements are actually executed in order to create all the required tables or drop tables as necessary. The way this is done is by using the following command.

`python manage.py sqlmigrate <app name> <migration version>`

If we go inside the app folder we will find a folder called migrations that actually contain all the migrations that we have made. The files in the migrations folder generally starts with a number like **0001**, **0002** in a sequence. This number is actually the migration version. This migration version is provided into the python sqlmigrate command in order to generate the sql statements. 

#### Objecttive

In the production server it may be necessary to run sql statements separately. In order to achieve that all we would ideally need to do is to simply have one command and that command would validate for errors and generate all sql statements. This should ideally happen with just one command. 