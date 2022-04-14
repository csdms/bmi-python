BMI for Python
==============

Python bindings for the CSDMS `Basic Model Interface <https://bmi.readthedocs.io>`_.

.. image:: https://zenodo.org/badge/179283861.svg
    :target: https://zenodo.org/badge/latestdoi/179283861
    :alt: DOI

.. image:: https://github.com/csdms/bmi-python/actions/workflows/test.yml/badge.svg
    :target: https://github.com/csdms/bmi-python/actions/workflows/test.yml
    :alt: Build Status

.. image:: https://anaconda.org/conda-forge/bmipy/badges/version.svg
    :target: https://anaconda.org/conda-forge/bmipy
    :alt: Anaconda-Server Badge

.. image:: https://anaconda.org/conda-forge/bmipy/badges/platforms.svg
    :target: https://anaconda.org/conda-forge/bmipy
    :alt: Anaconda-Server Badge

.. image:: https://anaconda.org/conda-forge/bmipy/badges/downloads.svg
    :target: https://anaconda.org/conda-forge/bmipy
    :alt: Anaconda-Server Badge

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
