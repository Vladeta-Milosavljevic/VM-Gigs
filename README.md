# VM-Gigs

Example job listing site project made using Django, Alpine Js, Jquery and Bootstrap 5


## This Project includes the following:

* Registration with email verification,
* Authentication,
* Authorisation,
* CRUD,
* Search,
* Pagination suitable for large number of pages,
* Sending the job aplication via email
* Custom decorators
* Writen tests for the project

### Dependencies

* virtial enviroment (example: virtualenv), pytohn, Django, MySql client and Pillow are required.
* Jquery and Alpine js are included in the project

### Installing


* Python install

```
python -m pip install
```

* Virtual enviroment install
  
```
pip install virtualenv
```

* Create virtual enviroment
* Note: virtual enviroment  and Djanog project need to be inside a single folder
  
```
virtualenv exampleName
```

* Activate virtual enviroment

```
exampleName\Scripts\activate
```

* Django install
  
```
pip install Django
```

* MySql client install

```
pip install mysqlclient
```

* Pillow install

```
pip install Pillow
```


* Bootstrap 5 install

```
pip install django-bootstrap-v5
```

* Place the project folder in the same folder as the virtual enviroment
* Navigate to the project folder in the ternimal
* Setup the database and run the migration

```
python manage.py migrate
```


### Executing the app

* Activate virtual enviroment
* Port for MySql is 3308, feel free to change to your local preferences it the settings.py file

```
exampleName\Scripts\activate
```

* Activate the local server
* Note: you need to be in the project folder (proba)

```
python manage.py runserver
```


## Author

Vladeta Milosavljevic

