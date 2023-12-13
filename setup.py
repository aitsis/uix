from setuptools import setup, find_packages
setup(
    
    name="uix",
    version = "1.0.0",
    description = "uix",
    author = "AIT",
    packages = find_packages(),
    exclude_package_data = {
        "uix": [ "*.pyc"]
    },
    python_requires = ">=3.6",
    long_description = "AIT UI uix",


    install_requires = [
        "Flask",
        "Flask-Cors",
        "Flask-SocketIO"
    ],
)