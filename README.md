
Freelance Connect - CSCI 427

# The Software Developer Network

# Synopsis

This website aims to become the foundation for which free lance software development work is posted and bid on. ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg

# Technology

We are using Django with python 3.5, along with html, css, js and bootstrap and a mysql back end (through django)

# Django Help

Tutorials:
how to use django and html forms: https://docs.djangoproject.com/en/1.10/topics/forms/

after installing django, clone repo and navigate to sdnSite folder. within that folder run 'python manage.py runserver' use the default IP provided followed by port 8000 (i.e. http://127.0.0.1:8000 ).

*when updating or adding new models for database, run 'python manage.py migrate' to make sure django applies changes to back end*

*when creating a new page directory use 'python manage.py startapp'*

# Bootstrap Help

resources:
https://github.com/dyve/django-bootstrap3/tree/develop/bootstrap3

# Setup

### Developing Locally

#### Dependencies
Python 3.5: https://www.python.org/downloads/release/python-350/

Pip:
https://pip.pypa.io/en/stable/installing/

Django 1.10:
After pip is installed, run the command `pip install django`

#### Build
Once the Dependencies are installed, pull files from the repository to your local machine. Go to the command line, and move to the folder in the project in which `manage.py` exists. For example, on my PC:

`cd C:\Users\Daddy Schurg\Documents\School\Senior yr 2\Spring 17\csci 427\SDN\SDN\sdnSite`

We must then initialize the database based on our Python Models class. To do this, run:

`python manage.py makemigrations`

Then:

`python manage.py migrate`

And finally, to start our local server:

`python manage.py runserver`

If the server build is successful, you will be given an IP address, usually http://127.0.0.1:8000/. If you go to this address, you will be 404'ed. Go to http://127.0.0.1:8000/home/ instead to find the home page.

# Website Structure

Our Structure so far:
  home

  --guest-index (http://127.0.0.1:8000/home/)
  --worker-index(http://127.0.0.1:8000/home/worker)
  --employer-index(http://127.0.0.1:8000/home/employer)

  accounts

  --login     (http://127.0.0.1:8000/accounts/login)
  --create worker (http://127.0.0.1:8000/accounts/new_worker)
  --create employer(http://127.0.0.1:8000/accounts/new_employer)

  posting

  --jobs      (http://127.0.0.1:8000/posting/job)
  --employment(http://127.0.0.1:8000/posting/employment)
  --for hire  (http://127.0.0.1:8000/posting/for_hire)
