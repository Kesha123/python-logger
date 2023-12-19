Python Logger
==============

Python Logger makes it easy to initialize a logger within the application scope. The Logger provides colorization and multiple ways to present and persist logs, including file and database storage. It allows you to set different logging levels for various handlers.

Install
-------

.. code-block:: bash

    pip install git+https://github.com/Kesha123/python-logger.git@v<latest-release-tag-number>

Available Handlers
------------------

.. list-table::
    :header-rows: 1

    * - Handler
      - HandlerLevel Argument Name
      - Description
    * - **Stream Handler**
      - stream
      - Terminal and command line output
    * - **File Handler**
      - file
      - Persist logs in specified file
    * - **MongoDB Handler**
      - mongodb
      - Persist logs in specified Mongo database

Use
---

In order to use a certain handler, pass it as an argument to ``HandlerLevel``

.. code-block:: python

    import logging
    from python_logger.Logger import Logger
    from python_logger.handlers import *

    handlers = HandlerLevel(stream=StreamHandler(level=logging.DEBUG))
    logger = Logger(handlers=handlers)
    logger.debug("Hello World!")

Logger
^^^^^^

.. list-table::
    :header-rows: 1

    * - Argument
      - Type
      - Description
      - Default Value
      - Available Values
    * - handlers
      - HandlerLevel
      - Defines available handlers
      - ``HandlerLevel(stream = StreamHandler())``
      -
    * - **colored_message**
      - bool
      - Message is colored (green, cyan, etc.)
      - True
      - True, False

HandlerLevel
^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Argument
      - Type
      - Default Value
    * - **stream**
      - StreamHandler
      - None
    * - **file**
      - FileHandler
      - None
    * - **mongodb**
      - FileHandler
      - None

StreamHandler
^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Argument
      - Type
      - Description
      - Default Value
      - Available Values
    * - **level**
      - int
      - Logging level
      - DEBUG
      - logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL

FileHandler
^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Argument
      - Type
      - Description
      - Default Value
      - Available Values
    * - **file**
      - str
      - Files where logs are stored.
      - logs.log
      -
    * - **level**
      - int
      - Logging level
      - DEBUG
      - logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL

MongoDBHandler
^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Argument
      - Type
      - Description
      - Default Value
      - Available Values
    * - **level**
      - int
      - Logging level
      - DEBUG
      - logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
    * - **connection_string**
      - str
      - Mongo Database connection string
      - None
      -
    * - **database**
      - str
      - Mongo Database Name
      - None
      -
    * - **collection**
      - str
      - Mongo Database Collection Name
      - None
      -

Logging Levels
---------------

.. list-table::
    :header-rows: 1

    * - Level
      - Code
    * - NOTSET
      - 0
    * - DEBUG
      - 10
    * - INFO
      - 20
    * - WARNING
      - 30
    * - ERROR
      - 40
    * - CRITICAL
      - 50
