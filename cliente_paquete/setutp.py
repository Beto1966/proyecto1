# setup.py
from setuptools import setup, find_packages

setup(
    name="cliente-paquete",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Aquí se incluirían dependencias si las hubiera
    author="Roberto Arriaga",
    author_email="robertcop7@gmail.com",
    description="Un paquete para modelar clientes en una página de compras.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/beto1966/cliente_paquete",  # Cambiar a la URL de tu repositorio
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)