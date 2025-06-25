Quick Start Guide
=================

A minimal set of commands or steps to get the app running locally.

Make sure you followed the steps in :ref:`installation_steps`.

1. Go in the project directory
    .. code-block:: sh

        cd path/to/oc-projet_13/
        # activate virtual environment
        source venv/bin/activate
        # cd in src folder
        cd src/


2. Start Django's server
    .. code-block:: sh

        python manage.py runserver

2. Start a gunicorn server
    .. code-block:: sh

        gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT # replace $PORT with the port you want your app to run on

4. Run Linting of the code
    .. code-block:: sh

        flake8

5. Run tests
    .. code-block:: sh

        pytest

Alternative with Docker
^^^^^^^^^^^^^^^^^^^^^^^

You can run the app without installing with our Docker image.

1. To run the app:
In the following command, replace sentry_dsn by your sentry DSN url if you want to track errors.
Also replace tag_name with the latest image tag from `Docker Hub repository <https://hub.docker.com/r/grompras/oc_hub/tags>`_

    .. code-block:: sh

       docker run -p 8009:8000 --name lettings_app -env PORT=8000 -env SENTRY_DSN=sentry_dsn grompras/oc_hub:tag_name

If this settings doesn't work for you refer to the docker run doc to customize the command:
`https://docs.docker.com/reference/cli/docker/container/run/`_


* Go back to : :doc:`installation`
* Next go to : :doc:`tech_stack`
