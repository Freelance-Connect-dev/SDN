
Freelance Connect - CSCI 427

# The Software Developer Network

# Synopsis

This website aims to become the foundation for which free lance software development work is posted and bid on.

#Technology

We are using Django, along with html, css, js and bootstrap and a mysql back end (through django)

#Django Help

Tutorials:
*post links here*

after installing django, clone repo and navigate to sdnSite folder. within that folder run 'python manage.py runserver' use the default IP provided followed by port 8000 (i.e. http://127.0.0.1:8000 ).

*when updating or adding new models for database, run 'python manage.py migrate' to make sure django applies changes to back end*

*when creating a new page directory use 'python manage.py startapp'*

#Website Structure

Our Structure so far:
  home
    guest-index (http://127.0.0.1:8000/home/)
    worker-index(http://127.0.0.1:8000/home/worker)
    employer-index(http://127.0.0.1:8000/home/employer)
  accounts
    login     (http://127.0.0.1:8000/accounts/login)
    create worker (http://127.0.0.1:8000/accounts/new_worker)
    create employer(http://127.0.0.1:8000/accounts/new_employer)
  posting
    jobs      (http://127.0.0.1:8000/posting/job)
    employment(http://127.0.0.1:8000/posting/employment)
    for hire  (http://127.0.0.1:8000/posting/for_hire)
