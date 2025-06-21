Installation
============

Prerequisites
-------------

* Git
* Python >= 3.13
* A Sentry account (optional)

.. _installation_steps:

Installation Steps
------------------

1. Clone the repo:
    .. code-block:: sh

        git clone https://github.com/GromPras/oc-projet_13.git
2. Create virtual environment:
    .. code-block:: sh

        cd /path/to/oc-projet_13
        python -m venv venv # or use your prefered environment manager
        sourve venv/bin/activate # to activate the environment
3. Install dependencies:
    .. code-block:: sh

        cd /path/to/oc-projet_13
        sourve venv/bin/activate
        pip install -r requirements.txt

4. Configure Variables:
    All the environment variables have default values that allow the app to run.
    However, the error tracking with Sentry won't work without a valid DSN key. If you want this functionality you will need to set the SENTRY_DSN environment variable to a valid DSN key from your sentry account. Then:
    1. Create a `.env` file in the root directory of the project:
        .. code-block:: sh

            cd /path/to/oc-projet_13
            touch .env

    2. Edit the `.env` file with your favorite text editor:
        .. code-block:: sh

            SENTRY_DSN=your_valid_dsn_key
