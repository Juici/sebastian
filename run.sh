#!/usr/bin/env bash

virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r ./requirements.txt
./run.py
deactivate
