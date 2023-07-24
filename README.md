# VM-Gigs

Example job listing site project made using Django, Alpine Js and Jquery


## This Project includes the following:

* Registration with email verification, authentication and authorisation,
* CRUD,
* Search,
* Pagination suitable for large number of pages,
* Sending the job aplication via email
* Custom decorators
* Writen tests for the project

### Dependencies

* virtial enviroment (example: virtualenv), pytohn, Django,MySql client and Pillow are required.
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


### Executing program

* Activate virtual enviroment
* Port for MySql is 3308, feel free to change to your local preferences

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



## Acknowledgments

Traversy media Laravel project (LaraGigs) was the ispiration for this Django project. My gratitude goes to Brad Traversy for both inspiration and guidance through many videos he made on the subject of Web Development.
