# BMI for Python

Python bindings for the CSDMS [Basic Model Interface](https://bmi.readthedocs.io).

![[Python][pypi-link]][python-badge]
![[DOI][doi-link]][doi-badge]
![[Build Status][build-link]][build-badge]
![[PyPI][pypi-link]][pypi-badge]
![[Build Status][anaconda-link]][anaconda-badge]

[anaconda-badge]: https://anaconda.org/conda-forge/bmipy/badges/version.svg
[anaconda-link]: https://anaconda.org/conda-forge/bmipy
[build-badge]: https://github.com/csdms/bmi-python/actions/workflows/test.yml/badge.svg
[build-link]: https://github.com/csdms/bmi-python/actions/workflows/test.yml
[doi-badge]: https://zenodo.org/badge/179283861.svg
[doi-link]: https://zenodo.org/badge/latestdoi/179283861
[pypi-badge]: https://badge.fury.io/py/bmipy.svg
[pypi-link]: https://pypi.org/project/bmipy/
[python-badge]: https://img.shields.io/pypi/pyversions/bmipy.svg

## Install

Install *bmipy* with *pip*,

```bash
pip install bmipy
```

If you're using Anaconda, you can also install *bmipy*
with conda from the *conda-forge* channel,

```bash
conda install bmipy -c conda-forge
```

To build and install *bmipy* from source,

```bash
pip install git+https://github.com/csdms/bmi-python.git
```

## Usage

```python
from bmipy import Bmi


class MyBmi(Bmi):

    def initialize(self, config_file):
        # Your implementation goes here
```

A complete sample implementation is given in the
<https://github.com/csdms/bmi-example-python>
repository.
