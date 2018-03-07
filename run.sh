#!/bin/bash

export FLASK_APP=$(pwd)/backend/core/app.py
export FITTRACK_DB_USER=""
export FITTRACK_DB_PASS=""
export FITTRACK_DB_HOST=""
export FITTRACK_DB_NAME=""

#################################################################
## db commands                                                  #
# python -m backend.core.db.manager db init                     #
# python -m backend.core.db.manager db migrate -m "users table" #
# python -m backend.core.db.manager db upgrade                  #
#################################################################

python -m flask run --debugger
