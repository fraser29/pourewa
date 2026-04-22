Usage
=====

Install
-------

.. code-block:: bash

   pip install pourewa

Command line
------------

Get help:

.. code-block:: bash

   pourewa --help

Print Orthanc status:

.. code-block:: bash

   pourewa -INFO

Print a summary of all studies:

.. code-block:: bash

   pourewa -A -S

Export selected studies to a directory:

.. code-block:: bash

   pourewa -s <STUDY_ID_1> <STUDY_ID_2> -E -o /path/to/output

Delete selected studies:

.. code-block:: bash

   pourewa -s <STUDY_ID_1> -D

Load DICOM files from a directory:

.. code-block:: bash

   pourewa -l /path/to/dicom_directory
