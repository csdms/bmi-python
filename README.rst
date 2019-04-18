BMI for Python
==============

Install
-------

Install *bmipy* with *pip*,

.. code-block:: bash

  $ pip install bmipy

If you're using Anaconda, you can also install *bmipy*
with conda from the *conda-forge* channel,

.. code-block:: bash

  $ conda install bmipy -c conda-forge


Usage
-----

.. code-block:: python

  from bmipy import Bmi


  class MyBmi(Bmi):

      def initialize(self, config_file):
          # Your implementation goes here
