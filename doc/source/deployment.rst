Deployment & Continuous Delivery
================================

This section describes how to deploy **oc-lettings-site** using our GitHub Actions workflow.

GitHub Actions Workflow
-----------------------

Our workflow, defined in `.github/workflows/build-python-app.yml`, has four main jobs:

1. **productionize**  

   * Runs on every push or PR.  
   * Sets up Python 3.12.  
   * Installs dependencies (`flake8`, `pytest`, `coverage`, plus `requirements.txt`).  
   * Lints with `flake8`.  
   * Runs tests under `pytest` with coverage, failing if coverage < 80%.

2. **build**  

   * Depends on **productionize**.  
   * Checks out the repo.  
   * Logs in to Docker Hub (using `DOCKERHUB_USERNAME` & `DOCKERHUB_TOKEN` secrets).  
   * Builds and pushes the Docker image tagged `grompras/oc_hub:${{ github.sha }}`.

3. **await-approval**  

   * Only on pushes to `main`.  
   * Pauses the workflow until a human approves the deployment (via the “deploy-approval” environment in GitHub).

4. **deploy**  

   * Runs after manual approval on `main`.  
   * Sends a POST request to your Render webhook (using the `WEBHOOK_URL` secret), passing the new image tag.

Secrets & Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **SENTRY_DSN**  
  Captured as an environment variable in **productionize** for test logging.  
* **DOCKERHUB_USERNAME**, **DOCKERHUB_TOKEN**  
  Used by `docker/login-action` to push to Docker Hub.  
* **WEBHOOK_URL**  
  The Render (or other hosting) webhook that triggers production deployment.  
* **PORT**  
  (If needed) your runtime port, set either in the container or in Compose/Render.

Triggering Deploys Manually
---------------------------

1. Merge a PR or push into `main`.  
2. Approve the “deploy-approval” step in the **Actions** tab.  
3. The **deploy** job will fire and invoke your webhook, rolling out the new Docker image.

Rollbacks
---------

* To revert, deploy an earlier Docker tag by manually invoking your hosting deploy hook with ``imgURL=docker.io/grompras/oc_hub:<previous-sha>``.  
* Make sure everything after *imgURL=* is url encoded.

Troubleshooting
---------------

* Check the **Actions** logs for failures in lint, test, build, or deployment steps.  
* Ensure all required secrets (``SENTRY_DSN``, ``DOCKERHUB_*``, ``WEBHOOK_URL``) are present in your repository settings.

With this workflow in place, every change to ``main`` passes through CI, requires approval, and then deploys automatically—providing a robust, audited pipeline for production updates.


* Go back to : :doc:`usage_guide`
