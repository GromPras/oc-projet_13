Quick Start Guide
=================

A minimal set of commands or steps to get the app running locally.

Make sure you followed the steps in :ref:`installation_steps`.

.. code-block:: sh
    # cd in the project directory
    cd path/to/oc-projet_13/src/

    # Run the server
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT # replace $PORT with the port you want your app to run on

    # Lint the code
    flake8

    # Run tests
    pytest

Alternative with Docker
^^^^^^^^^^^^^^^^^^^^^^^

1. Run the app:
In the following command, replace sentry_dsn by your sentry DSN url if you want to track errors.
Also replace tag_name with the latest image tag from `Docker Hub repository<https://hub.docker.com/r/grompras/oc_hub/tags>`__

   .. code-block:: sh

        docker run -p 8009:8000 --name lettings_app -env PORT=8000 -env SENTRY_DSN=sentry_dsn grompras/oc_hub:tag_name

If this settings doesn't work for you refer to the docker run doc to customize the command:
`https://docs.docker.com/reference/cli/docker/container/run/`_
.. _a link: https://docs.docker.com/reference/cli/docker/container/run/
