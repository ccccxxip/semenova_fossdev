from setuptools import setup, find_packages

setup(
    name = "tax",
    version = "0.0.0", 
    package_dir = {"testing/frameworks/src/tax"},
    packages = find_packages(where="src")
)
