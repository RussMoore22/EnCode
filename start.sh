#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P)
cd "$parent_path"
echo $parent_path

f="runserver"

if [ "$#" -eq "0" ] 
then
        echo "No arguments supplied."
else
    while getopts c:f: flag
    do
        case "${flag}" in
            f) f=${OPTARG};;
        esac
    done
fi

source "venv/bin/activate"

if [ -e ./db.sqlite3 ]
then
    echo "Database does exists..."
else
    echo "No database found creating..."
    python manage.py makemigrations
    python manage.py migrate
fi

python manage.py $f
