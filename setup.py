from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="litecoinrpc",
    version="0.0.1",
    description="Litecoin RPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitwyre/python-litecoinrpc",
    author="Jeff Garzik, Bitwyre Technologies LLC",
    author_email="jgarzik@pobox.com, dev@bitwyre.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="financial exchange cryptocurrency",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=[],  # Optional
    extras_require={"dev": ["check-manifest", "pep8", "mypy"], "test": ["coverage", "pytest"]},
    project_urls={
        "Bug Reports": "https://github.com/bitwyre/python-litecoinrpc/issues",
        "Funding": "https://bitwyre.com",
        "Say Thanks!": "http://bitwyre.gives",
        "Source": "https://github.com/bitwyre/python-litecoinrpc/",
    },
)
