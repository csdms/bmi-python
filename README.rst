BMI for Python
==============

Python bindings for the CSDMS `Basic Model Interface <https://bmi-spec.readthedocs.io>`_.

Install
-------

Install *bmipy* with *pip*,

.. code-block:: bash

  $ pip install bmipy

If you're using Anaconda, you can also install *bmipy*
with conda from the *conda-forge* channel,

.. code-block:: bash

  $ conda install bmipy -c conda-forge

To build and install *bmipy* from source,

.. code-block:: bash

  $ git clone https://github.com/csdms/bmi-python
  $ cd bmi-python
  $ pip install .

Usage
-----

.. code-block:: python

  from bmipy import Bmi


  class MyBmi(Bmi):

      def initialize(self, config_file):
          # Your implementation goes here

A complete sample implementation is given in the
https://github.com/csdms/bmi-example-python
repository.
