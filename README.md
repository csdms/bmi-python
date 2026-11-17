# BMI for Python

Python bindings for the CSDMS [Basic Model Interface](https://bmi.readthedocs.io).

![[Python][pypi-link]][python-badge]
![[DOI][doi-link]][doi-badge]
![[Build Status][build-link]][build-badge]
[![bmipy package version][pypi-badge]][pypi-link]
[![BMI specification version][bmi-badge]][bmi-link]

[build-badge]: https://github.com/csdms/bmi-python/actions/workflows/test.yml/badge.svg
[build-link]: https://github.com/csdms/bmi-python/actions/workflows/test.yml
[doi-badge]: https://zenodo.org/badge/179283861.svg
[doi-link]: https://zenodo.org/badge/latestdoi/179283861
[bmi-badge]: https://img.shields.io/badge/BMI_specification-2.0-blue
[bmi-link]: https://github.com/csdms/bmi/releases/tag/v2.0
[pypi-badge]: https://img.shields.io/pypi/v/bmipy?label=bmipy
[pypi-link]: https://pypi.org/project/bmipy/
[python-badge]: https://img.shields.io/pypi/pyversions/bmipy.svg

## Package and specification versions

Note that a new *bmipy* release does not necessarily change the supported BMI
specification. You can check the package version independently of the interface
specification version:

```python
from bmipy import __version__
from bmipy.bmi2_0 import BMI_VERSION

print(__version__)  # bmipy package version
print(BMI_VERSION)  # Supported BMI specification
```

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
from bmipy.bmi2_0 import Bmi


class MyBmi(Bmi):

    def initialize(self, config_file):
        # Your implementation goes here
```

The `bmipy.bmi2_0` module explicitly selects the BMI 2.0 specification.
The existing `from bmipy import Bmi` and `from bmipy.bmi import Bmi` imports
remain available for compatibility.

A complete sample implementation is given in the
<https://github.com/csdms/bmi-example-python>
repository.
