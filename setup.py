import os.path
import sys

from setuptools import setup

sys.path.append(os.path.dirname(__file__))

# See pyproject.toml for project metadata
setup(
    name="bmipy",  # need by GitHub dependency graph
)
