#!/bin/sh

python3 manage.py makemigrations notifyer
echo "Need Migrate"
python3 manage.py migrate notifyer