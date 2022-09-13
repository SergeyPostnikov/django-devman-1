# Bank security console
The security console is a site that can be connected to a remote database with visits and pass cards of our bank employees.

The site requires access to the database.

## before start you have to:
- create .env file on project directory and add record:  
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME  

## for installation: 
```
git clone https://github.com/SergeyPostnikov/django-devman-1
pip install -r requirements.txt
```
## for launch:
The site can be launched using the standard Django development server.
```
python manage.py ruserver
```
