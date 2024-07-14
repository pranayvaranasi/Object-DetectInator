#!/bin/bash

# create the virutual environment in the project root
python3 -m venv flaskapp_env

# activate the virtual environment 
source flaskapp_env/bin/activate
#Run App file
python3 run app.py
