from setuptools import find_packages, setup


NAME = "loadero_python"
VERSION = "0.0.1"
REQUIRES = ["urllib3==1.26.9", "tabulate==0.8.9", "python-dateutil==2.8.2"]


setup(
    name=NAME,
    version=VERSION,
    description="Python client for Loadero API",
    author="Loadero Team",
    author_email="support@loadero.com",
    url="https://github.com/loadero/loadero-python",
    packages=find_packages(),
    install_requires=REQUIRES,
    python_requires=">=3.6",
)
