Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.7
* pip3
* pipenv
* git

on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python37 python3-pip
    sudo pip3 install pipenv
   
## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.djangotdd.tk

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.djangotdd.tk

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
