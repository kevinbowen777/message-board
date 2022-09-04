## message_board - A simple web message board

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/message_board.svg)](https://github.com/kevinbowen777/message_board/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

message_board is a demonstration of simple Django functionality

---
## Features

 - Post simple text messages
 - User registration with email verification & social(GitHub) login
 - Bootstrap4 & crispy-forms decorations
 - Customizable user profiles with bio, profile picture & country flags
 - Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

### Installation
 - `git clone https://github.com/kevinbowen777/message_board.git`
 - `cd message_board`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/


### Live Demo on Heroku:
 - [message_board live demo](https://kbowen-django-message-board.herokuapp.com/)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/message_board/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/message_board/issues)
      to view currently open bug reports or open a new issue.
