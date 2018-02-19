#!/bin/bash

export FLASK_APP=$(pwd)/backend/core/app.py

python -m flask run --debugger
