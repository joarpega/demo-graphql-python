# Demo Graphql Python


## Previous requirements
* System operative based on unix or linux 
* docker and docker-compose


1. Create virtual environment
```
$ python3 -m venv env

# Load virtual environment
$ source env/bin/activate

```
2. Install wheel 
```bash
pip install wheel
```
3. Install grapgene
```
pip install graphene
```
4. Install Django
```
pip install Django==3.0.8
```
5. Check installed packages 
```
pip freeze
```
6. Show Django packages with django-admin 

---

```
pip install django
pip install graphene-django
pip install django-filter
pip install django-graphql-jwt

django-admin startapp api # crea aplicacion api


python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
```
