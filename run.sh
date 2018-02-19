#!/bin/bash

export FLASK_APP=$(pwd)/backend/core/app.py

python -m flask run --host=0.0.0.0 --debugger
