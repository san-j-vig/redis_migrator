# Description
This application enables migrate/transfer of data between Redis instances. The code is written in Python 3.

# Setup
1. Install python dependencies by running `python -m pip install -r requirements.txt` 
2. Create a `config.py` file with the help of `config.example.py` in the root of this repo

# How to run
Browse to root of this repo and execute  
```python
python app.py
```

# Test Connection
After following all the steps in [Setup](#setup) section, execute the following command:
```python
python test_conn.py
```