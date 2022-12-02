## message-board

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/message-board.svg)](https://github.com/kevinbowen777/message-board/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

message-board is a simple text posting application built with the Django web framework

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features

 - Application
     - Post simple text messages
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - Basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, 3.11, and 3.12
         - black (`nox -s black`)
         - Sphinx documentation generation (`nox -s docs`)
         - linting (`nox -s lint`)
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing) (`nox -s safety`)
         - pytest sessions with coverage (`coverage run -m pytest`)
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

### Installation
 - `git clone https://github.com/kevinbowen777/message-board.git`
 - `cd message-board`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it message-board-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11, 3.12
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### Application Demo

TBD

---

### Screenshots

### Home
![Home](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_home.png)

### Message Index
![Message Index](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_index.png)

### Profile Page
![Profile Page](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_profile-page.png)

### Login Page
![Login Page](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_sign-in.png)

### New Message
![New Message](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_new-message.png)

### Edit Message
![Edit Message](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_edit-message.png)

### Delete Message
![Delete Message](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_delete-message.png)

### Email Address management
![Email Address management](https://github.com/kevinbowen777/message-board/blob/master/images/message-board_email-addresses.png)

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/message-board/issues)
      to view currently open bug reports or open a new issue.
