from setuptools import setup

import versioneer


setup(
    name="bmi",
    version=versioneer.get_version(),
    description="Basic Model Interface",
    author="Eric Hutton",
    author_email="huttone@colorado.edu",
    url="http://csdms.colorado.edu",
    setup_requires=["setuptools"],
    cmdclass=versioneer.get_cmdclass(),
)
