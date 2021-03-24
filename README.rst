.. raw:: html

   <p align="left">

   <a href="https://zenodo.org/badge/latestdoi/179283861">
	 <img src="https://zenodo.org/badge/179283861.svg"
	 alt="DOI"></a>

   <a href='https://travis-ci.org/csdms/bmi-python'>
	 <img src='https://travis-ci.org/csdms/bmi-python.svg?branch=master'
	 alt='Build Status'></a>

   <a href='https://anaconda.org/conda-forge/bmipy'>
	 <img src='https://anaconda.org/conda-forge/bmipy/badges/version.svg'
	 alt='Anaconda-Server Badge'></a>

   <a href='https://anaconda.org/conda-forge/bmipy'>
	 <img src='https://anaconda.org/conda-forge/bmipy/badges/platforms.svg'
	 alt='Anaconda-Server Badge'></a>

   <a href='https://anaconda.org/conda-forge/bmipy'>
	 <img src='https://anaconda.org/conda-forge/bmipy/badges/downloads.svg'
	 alt='Anaconda-Server Badge'></a>

   </p>


BMI for Python
==============

Python bindings for the CSDMS `Basic Model Interface <https://bmi.readthedocs.io>`_.

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
