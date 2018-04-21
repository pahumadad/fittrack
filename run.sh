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


help() {
    echo -e "usage:"
    echo -e "\t[-s | --start]\tto start flask app"
    echo -e "environments to set:"
    echo -e "\tFLASK_APP"
    echo -e "\tFITTRACK_DB_USER"
    echo -e "\tFITTRACK_DB_PASS"
    echo -e "\tFITTRACK_DB_HOST"
    echo -e "\tFITTRACK_DB_NAME"
    echo -e "db commands"
    echo -e "\tpython -m backend.core.db.manager db init"
    echo -e "\tpython -m backend.core.db.manager db migrate -m 'message'"
    echo -e "\tpython -m backend.core.db.manager db upgrade"
    exit 0
}

case "$1" in
    -s | --start)
        python -m flask run --debugger
        ;;
    *)
        help
esac
