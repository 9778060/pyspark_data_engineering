==========================
Pyspark. Data engineering
==========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License: MIT

|badge1| |badge2|

Local **PySpark Data Engineering** playground built around a Docker-based stack
for experimenting with batch ETL, HDFS storage, and Airflow-orchestrated jobs.

Repository overview
===================

This repository contains:

* Docker-based environment (Spark + Hadoop/HDFS + Airflow + notebooks)
* Example PySpark applications and helper scripts
* Airflow DAGs to orchestrate Spark ETL
* Notes/cheatsheets with common Spark/HDFS commands

Project structure
=================

Top-level folders (see the repository root):

* ``dags/`` – Airflow DAG definitions.
* ``spark-apps/`` – PySpark applications (ETL / transformations / utilities).
* ``hadoop-config/`` – Hadoop / HDFS configuration used by the containers.
* ``my_notebooks/`` – personal/learning notebooks.
* ``notebooks/ data/`` – sample datasets used by notebooks/apps.
* ``spark-events/`` – Spark event logs for the Spark History Server.

Top-level files:

* ``docker-compose.yml`` – brings up the local data-engineering stack.
* ``Dockerfile.airflow`` / ``Dockerfile.history`` – custom images used by the compose stack.
* ``requirements.txt`` – Python dependencies for local development.
* ``help_commands.txt`` / ``help_spark.txt`` – command references and tips.
* ``readme.txt`` – quick notes.

Prerequisites
=============

* Docker + Docker Compose
* (Optional) Python 3.12+ if you want to run/format/lint code locally

Local Python environment (optional)
===================================

Create and activate a virtual environment:

.. code-block:: bash

    python3.12 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Start the stack
===============

Bring up all services:

.. code-block:: bash

    docker compose up -d

Useful UIs and endpoints depend on your ``docker-compose.yml`` ports mapping.
Typical services you may have in this stack:

* Airflow Web UI
* Spark Master UI
* Spark History Server UI
* HDFS NameNode UI
* Jupyter Notebook/Lab UI

To check what is exposed on your machine:

.. code-block:: bash

    docker compose ps

Run a PySpark job
=================

A common pattern is to submit a job to the Spark master container and point it to
an app in ``spark-apps/``.

Example (adjust container name and path to match your compose file):

.. code-block:: bash

    docker exec -it spark-master spark-submit /spark-apps/<your_app>.py

HDFS quick commands
===================

If your stack includes HDFS, you can run ``hdfs`` commands from the appropriate
container (often the NameNode):

.. code-block:: bash

    docker exec -it namenode hdfs dfs -ls /
    docker exec -it namenode hdfs dfs -mkdir -p /data
    docker exec -it namenode hdfs dfs -put /path/in/container/file.csv /data/

Airflow
=======

DAGs live in ``dags/``. Once the Airflow services are running, the scheduler will
discover DAG files from this folder (depending on your compose volume mapping).

Tips:

* Make sure the DAG file ends with ``.py``.
* Check Airflow logs if a DAG doesn’t show up or is failing to parse.

Additional functionality/features:
...

Credits
=======

Authors
~~~~~~~

* 9778060
* Special credits and thanks to Chandra Venkat for his great PySpark course, tutorials and resources (https://www.udemy.com/user/chandra-venkat-4/)

Maintainers
~~~~~~~~~~~

This repository is maintained by **9778060**.
