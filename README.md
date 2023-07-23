### Run my project
**Requirements**
- Python 3.11
- virtual environment 

To install python virtual environment use this command on **Unix/ MacOS**
```python3 -m pip install --user virtualenv```
In **windows** platform use this command.
```py -m pip install --user virtualenv```

After successful installation of virtual environment you have to initiate a virtual environment by this command **on Unix/MacOS**: 
```python3 -m venv env```
**on Windows**:
```python -m venv env```

After initaiting you have to activate it.
**on Unix/MacOS**:
```source env/bin/activate```
**on Windows**:
```env\Scripts\activate```

Now, you have to install necessary packeges. The `requriements.txt` file contains the list of them. To install them you can use this command ```pip install -r requirements.txt```