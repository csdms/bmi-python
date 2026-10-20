"""The Basic Model Interface (BMI) for Python."""

from __future__ import annotations

from bmipy._stub import BmiStub
from bmipy._version import __version__
from bmipy.bmi2_0 import BMI_VERSION
from bmipy.bmi2_0 import Bmi

__all__ = ["__version__", "BMI_VERSION", "Bmi", "BmiStub"]
