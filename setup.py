from distutils.core import setup

setup(
    # Application name:
    name="payment_svc",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Mudit Somani",
    author_email="mudit.somani@bigbasket.com",

    # Packages
    packages=["tests", "web"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",

    ],
)