from setuptools import setup, find_packages


setup(
    name="optativa_pycicd_jpg",
    version="1.0.0",
    author="Javier Pomares Gomez",
    author_email="javierpomaresgomez@gmail.com",
    description="Proyecto de practica",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
    ],
)