"""Loadero-Python setup module"""

import pathlib
from setuptools import find_packages, setup


root_path = pathlib.Path(__file__).parent.resolve()
long_description = (root_path / "README.md").read_text(encoding="utf-8")


setup(
    name="loadero_python",
    version="1.2.1",
    description="Python client for Loadero API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loadero/loadero-python",
    author="Loadero Team",
    author_email="support@loadero.com",
    license="GPLv3",
    classifiers=[
        # https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="loadero",
    project_urls={
        "Documentation": "https://loadero.github.io/loadero-python/",
        "Source": "https://github.com/loadero/loadero-python",
        "Tracker": "https://github.com/loadero/loadero-python/issues",
        "Loadero": "https://loadero.com/",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.7, <4",
    install_requires=[
        "urllib3==1.26.17",
        "python-dateutil==2.8.2",
    ],
)
