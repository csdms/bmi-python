from .bmi import Bmi


__all__ = ["Bmi"]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
