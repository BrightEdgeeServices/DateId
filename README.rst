======
DateId
======

+-----------+------------------------------------------------------------------------------------+
|**General**| |maintenance_y| |semver| |license|                                                 |
+-----------+------------------------------------------------------------------------------------+
|**CI**     | |gh_ci| |codestyle| |codecov|                                                      |
+-----------+------------------------------------------------------------------------------------+
|**PyPI**   | |pypi_release| |pypi_py_versions| |pypi_status| |pypi_format| |pypi_downloads|     |
+-----------+------------------------------------------------------------------------------------+
|**Github** | |gh_issues| |gh_language| |gh_last_commit| |gh_deployment|                         |
+-----------+------------------------------------------------------------------------------------+




Installation
------------

#. Since this is intended for experimental purposes, it is recommended to create a virtual environment to experiment for installation.
#. Set the following environment variables in the virtual environment.  Set these in your IDE as well.
#. Start Docker.  The ``docker-rebuild.bat`` script will git docker up and running.
#. The setup and installation is for Windows.  Feel free to add contribute to get it running on Linux as well.

.. code-block:: bash

    python -m venv ./DataId_venv
    pip install FastAPIexample
    pre-commit install
    SET MYSQL_HOST=localhost
    SET MYSQL_ROOT_PWD=N0tS0S3curePassw0rd
    SET MYSQL_TCP_PORT_EXAMPLES=50002
    SET SQLALCHEMY_SILENCE_UBER_WARNING=1
    docker-rebuild.bat


Tests
-----

#. This project uses ``pytest`` to run tests.
#. There are various settings combinations in the ``[tool.pytest.ini_options]`` section of the pyproject.toml file that can used by commenting it out.
#. This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

.. code-block:: bash

    pytest


Contributing
------------

Naming Conventions
~~~~~~~~~~~~~~~~~~

#. File names
    #. Not knowing what's to come and what will be added, it is difficult to determine a naming convention for source, test and other file names.  The owner will therefore be a "benevolent dictator" to rename and change names.
    #. Link the file name of the source code and the test so that it is easily linked.
#. Branch names
    "enhancement" | "bug" | "hotfix"/< ticket_nr>_<description>

    where
        enhancement - Planned improvement or addition to functionality; non-urgent.

        bug - An error or defect causing incorrect or unexpected behavior; typically fixed in regular development cycles.

        hotfix - An urgent, critical fix applied directly to the live environment, often bypassing regular development cycles.

        ticket_nr: Ticket number assigned to the issue in GitHub.  Once an issue is registered, the owner will assign a ticket.

        description: GitHub issue title or combination of titles is more than one issue is addressed.


Releasing
~~~~~~~~~
For the purpose of push and release of code two script files are included.  Use there two files to files to make life a
bit easier.  The scripts make use of the ``gitit`` module to simplify tasks.

#. ``push.bat`` - Use this script to push branches to GitHub repository.  In principle it does the following:

    usage: push message

    e.g. push "Changed the Infinite Improbability Drive"

    #. .rst syntax check
    #. git add -A
    #. git commit -m message (with `pre-commit` including `black` and `flake8`)
    #. git push --all

#. ``release.bat`` - Use this script to push a new tag and release to the GitHub repository.  Remember to change the version number in the setup.cfg else the workflow will fail.

    usage: release version  The version will match the release and the tag. Only issue a release once a push.bat was successful.  In principle it does the following:

    e.g. release 1.2.3

    #. Commit the changes
    #. Create and push the release tag with the correct naming conventions.
    #. Checkout master since it assumes that the branch is now merged with master and will be deleted.
    #. display a list of all the current branches as a reminder to delete the branch on completion.


.. General

.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-?-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-%E2%9C%94-green.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - intended

.. |license| image:: https://img.shields.io/pypi/l/DateId
    :target: https://github.com/BrightEdgeeServices/DateId/blob/master/LICENSE
    :alt: License

.. |semver| image:: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square
    :target: https://semver.org/
    :alt: Semantic Versioning - 2.0.0

.. |codestyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style Black


.. CI

.. |pre_commit_ci| image:: https://img.shields.io/github/actions/workflow/status/BrightEdgeeServices/DateId/pre-commit.yml?label=pre-commit
    :target: https://github.com/BrightEdgeeServices/DateId/blob/master/.github/workflows/pre-commit.yml
    :alt: Pre-Commit

.. |gh_ci| image:: https://github.com/BrightEdgeeServices/DateId/actions/workflows/01-pre-commit-and-document-check.yaml/badge.svg)
    :target: https://github.com/BrightEdgeeServices/DateId/actions/workflows/01-pre-commit-and-document-check.yaml
    :alt: Test status

.. |gha_docu| image:: https://img.shields.io/readthedocs/DateId
    :target: https://github.com/BrightEdgeeServices/DateId/blob/master/.github/workflows/check-rst-documentation.yml
    :alt: Read the Docs

.. |codecov| image:: https://img.shields.io/codecov/c/github/BrightEdgeeServices/DateId
   :alt: Codecov
    :target: https://app.codecov.io/gh/BrightEdgeeServices/DateId
    :alt: CodeCov


.. PyPI

.. |pypi_release| image:: https://img.shields.io/pypi/v/DateId
    :target: https://pypi.org/project/DateId/
    :alt: PyPI - Package latest release

.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/DateId
    :target: https://pypi.org/project/DateId/
    :alt: PyPI - Supported Python Versions

.. |pypi_format| image:: https://img.shields.io/pypi/wheel/DateId
    :target: https://pypi.org/project/DateId/
    :alt: PyPI - Format

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/DateId
    :target: https://pypi.org/project/DateId/
    :alt: PyPI - Monthly downloads

.. |pypi_status| image:: https://img.shields.io/pypi/status/DateId
    :target: https://pypi.org/project/DateId/
    :alt: PyPI - Status


.. GitHub

.. |gh_issues| image:: https://img.shields.io/github/issues-raw/BrightEdgeeServices/DateId
    :target: https://github.com/BrightEdgeeServices/DateId/issues
    :alt: GitHub - Issue Counter

.. |gh_language| image:: https://img.shields.io/github/languages/top/BrightEdgeeServices/DateId
    :target: https://github.com/BrightEdgeeServices/DateId
    :alt: GitHub - Top Language

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/BrightEdgeeServices/DateId/master
    :target: https://github.com/BrightEdgeeServices/DateId/commit/master
    :alt: GitHub - Last Commit

.. |gh_deployment| image:: https://img.shields.io/github/deployments/BrightEdgeeServices/DateId/pypi
    :target: https://github.com/BrightEdgeeServices/DateId/deployments/pypi
    :alt: GitHub - PiPy Deployment
