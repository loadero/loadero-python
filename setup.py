from setuptools import find_packages, setup


NAME = "loadero_python"
VERSION = "0.0.1"
REQUIRES = [
    # "urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"
]


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
    # license
)
