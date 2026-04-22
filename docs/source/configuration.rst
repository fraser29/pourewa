Configuration
=============

``pourewa`` reads settings from a ``POUREWA.conf`` file.

Configuration search order
--------------------------

The config loader checks the following locations in order:

#. ``pourewa/POUREWA.conf`` (package default)
#. ``~/POUREWA.conf``
#. ``~/.POUREWA.conf``
#. ``~/.config/POUREWA.conf``
#. Path specified by environment variable ``POUREWA_CONF``

Example configuration
---------------------

.. code-block:: ini

   [app]
   environment=test
   debug=True
   LOG_FILE_NAME=
   ORTHANC_URL=127.0.0.1
   ORTHANC_PORT=80
   ORTHANC_EXPOSED=orthanc
   ORTHANC_USERNAME=demo
   ORTHANC_PASSWORD=demo
