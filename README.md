### Run my project
**Requirements**
- Python 3.11
- virtual environment 

To install python virtual environment use this command on **Unix/ MacOS**
```python3 -m pip install --user virtualenv```
In **windows** platform use this command.
```py -m pip install --user virtualenv```

After successful installation of virtual environment you have to initiate a virtual environment. Beform that make sure that you're in the project directory(The directory that you have downloaded from github). Now initate virtual environment by this command **on Unix/MacOS**: 
```python3 -m venv env```
**on Windows**:
```python -m venv env```

After initaiting you have to activate it.
**on Unix/MacOS**:
```source env/bin/activate```
**on Windows**:
```env\Scripts\activate```

Now, you have to install necessary packeges. The `requriements.txt` file contains the list of them. To install them you can use this command ```pip install -r requirements.txt```. 


Now you can run the project. To do that you have to navigae to `backend` directory. After entering the directory you can run the project with this command ```python manage.py runserver```. 

*I hope it will work fine.*