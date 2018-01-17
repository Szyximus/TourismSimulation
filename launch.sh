#!/bin/bash

pip install -r requirements.txt
sudo PYTHONPATH="`pwd`/src:`pwd`" python3 src/main.py