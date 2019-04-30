from setuptools import find_packages, setup

import versioneer


setup(
    name="bmipy",
    version=versioneer.get_version(),
    description="Basic Model Interface for Python",
    long_description=open("README.rst").read(),
    author="Eric Hutton",
    author_email="huttone@colorado.edu",
    url="http://csdms.colorado.edu",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    setup_requires=["setuptools"],
    install_requires=["black", "click", "jinja2", "numpy"],
    packages=find_packages(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={"console_scripts": ["bmipy-render=bmipy.cmd:main"]},
)
