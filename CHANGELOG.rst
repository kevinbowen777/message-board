.. _`changelog`:

=========
Changelog
=========

``message-board`` issues are filed on `GitHub <https://github.com/kevinbowen777/message-board/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

message-board 0.3.6 (2026-09-07)
================================

Contributor-facing changes
--------------------------

-  (`#616 <https://github.com/kevinbowen777/message-board/616>`_): Update django-allauth to 65.19.1

-  (`#616 <https://github.com/kevinbowen777/message-board/616>`_): Update gunicorn to 26.1.0

-  (`#616 <https://github.com/kevinbowen777/message-board/616>`_): Update django-debug-toolbar to 7.1.1

-  (`#616 <https://github.com/kevinbowen777/message-board/616>`_),  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update nox to 2026.8.17

-  (`#628 <https://github.com/kevinbowen777/message-board/628>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update psycopg to 3.3.5

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update django-debug-toolbar to 8.0.0

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update djlint to 1.45.2

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update django-allauth to 65.19.2

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Upgrade environs to 15.2.0

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Upgrade gunicorn to 26.2.0

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Update towncrier to 26.9.0


New features
------------

-  (`#636 <https://github.com/kevinbowen777/message-board/636>`_): Upgrade Django to 6.1.1

message-board 0.3.5 (2026-08-18)
================================

Improved documentation
----------------------

-  (`#605 <https://github.com/kevinbowen777/message-board/605>`_): Add towncrier 25.8.0.


New features
------------

-  (`#630 <https://github.com/kevinbowen777/message-board/630>`_): Upgrade to Django 6.0.8

message-board 0.3.4 (2026-07-30)
================================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#609 <https://github.com/kevinbowen777/message-board/609>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#626 <https://github.com/kevinbowen777/message-board/626>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#620 <https://github.com/kevinbowen777/message-board/620>`_): Drop support for Python 3.11.


New features
------------

-  (`#587 <https://github.com/kevinbowen777/message-board/587>`_): Upgrade Django to 6.0.7.

message-board 0.3.3 (2025-05-04)
================================

Contributor-facing changes
--------------------------

-  (`#534 <https://github.com/kevinbowen777/message-board/534>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#530 <https://github.com/kevinbowen777/message-board/530>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#529 <https://github.com/kevinbowen777/message-board/529>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#535 <https://github.com/kevinbowen777/message-board/535>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#538 <https://github.com/kevinbowen777/message-board/538>`_): Replace safety package with pip-audit.

message-board 0.3.2 (2025-01-18)
================================

Contributor-facing changes
--------------------------

-  (`#472 <https://github.com/kevinbowen777/message-board/472>`_): Add support for Python 3.13

-  (`#512 <https://github.com/kevinbowen777/message-board/512>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#504 <https://github.com/kevinbowen777/message-board/504>`_): Upgrade Django to 5.1.4

message-board 0.3.0 (2023-12-30)
================================

Contributor-facing changes
--------------------------

- : Upgrade Poetry to 1.7.1.

-  (`#203 <https://github.com/kevinbowen777/message-board/203>`_): Migrate to non-root Docker user & venv.

-  (`#384 <https://github.com/kevinbowen777/message-board/384>`_): Update Python to 3.12.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#368 <https://github.com/kevinbowen777/message-board/368>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#380 <https://github.com/kevinbowen777/message-board/380>`_): Upgrade to Django 5.0.

message-board 0.2.0 (2023-05-21)
================================

Contributor-facing changes
--------------------------

-  (`#240 <https://github.com/kevinbowen777/message-board/240>`_): Install ruff. Drop flake8-* packages.

message-board 0.1.0 (2023-05-08)
================================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#200 <https://github.com/kevinbowen777/message-board/200>`_): Migrate from SQLite to PostgreSQL

-  (`#223 <https://github.com/kevinbowen777/message-board/223>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

- : Add Sphinx for documentation


New features
------------

-  (`#241 <https://github.com/kevinbowen777/message-board/241>`_): Upgrade to Django 4.2.

message-board 0.0.1 (2022-02-23)
================================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Build Docker support for Heroku deployment.

- : Support Django 4.0.3


Miscellaneous internal changes
------------------------------

- : Initial commit
