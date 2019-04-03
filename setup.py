from setuptools import find_packages, setup

import versioneer


setup(
    name="bmi",
    version=versioneer.get_version(),
    description="Basic Model Interface",
    author="Eric Hutton",
    author_email="huttone@colorado.edu",
    url="http://csdms.colorado.edu",
    setup_requires=["setuptools"],
    packages=find_packages(),
    cmdclass=versioneer.get_cmdclass(),
)
