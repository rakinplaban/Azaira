### Run my project
Several ways to run this project:
###### Way 1:
I have dockerized this project. So to run it, just clone this github repo and enter these commands:
1. docker pull rakin235/test-web:latest
2. docker pull rakin235/postgres:latest
3. docker-compose up


###### Way 2:
**Requirements**
- Python 3.11
- virtual environment 
- PostgreSQL

To install python virtual environment use this command on **Unix/ MacOS**
```python3 -m pip install --user virtualenv```
In **windows** platform use this command.
```py -m pip install --user virtualenv```

After successful installation of virtual environment you have to initiate a virtual environment. Beform that make sure that you're in the project directory(The directory that you have downloaded from github). Now initate virtual environment by this command **on Unix/MacOS**: 
```python3 -m venv env```
**on Windows**:
```python -m venv env```

I am using **PostgreSQL** in this project. So after installing it you have to configure database server with HOST **db** and database **test**.

After initaiting you have to activate it.
**on Unix/MacOS**:
```source env/bin/activate```
**on Windows**:
```env\Scripts\activate```

Now, you have to install necessary packeges. The `requriements.txt` file contains the list of them. To install them you can use this command ```pip install -r requirements.txt```. 


This time you'll need to migrate database. Use these commands respectively, ```python backend/manage.py makemigrations project``` and ```python backend/manage.py migrate```.


Now you can run the project. To do that you have to run the project with this command ```python backend/manage.py runserver```. 

**Note:** *It work on my machine but theres probability to not to run on your.*