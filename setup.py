import os.path
import sys
from setuptools import setup

sys.path.append(os.path.dirname(__file__))

import versioneer

setup(
    name="bmipy",  # need by GitHub dependency graph
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
