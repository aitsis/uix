from setuptools import setup, find_packages

setup(
    name='uix',  # Replace with your package's name
    version='0.1',            # The initial release version
    author='AIT',       # Your name
    author_email='info@ait.com.tr',  # Your email
    description='A new UI Project for python',  # Short description
    long_description=open('README.md').read(),  # Long description read from the readme file
    long_description_content_type='text/markdown',  # This is important for markdown files
    url='https://github.com/aitsis/uix',  # Link to your project's GitHub repo
    packages=find_packages(where='src'),  # Where to find the source code
    package_dir={'': 'src'},  # Tell distutils packages are under src
    install_requires=[
        # List of dependencies
        
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of the package
)
