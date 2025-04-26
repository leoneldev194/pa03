from setuptools import setup, find_packages

setup(
    name="proyecto_tdd_orm",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "sqlalchemy",
    ],
)