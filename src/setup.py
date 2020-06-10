import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sparkmonitor-stvoutsin", # Replace with your own username
    version="0.0.1",
    author="Stelios Voutsinas",
    author_email="stv@roe.ac.uk",
    description="Tool for accessing the Spark REST API",
    long_description="Tool for accessing the Spark REST API",
    long_description_content_type="text/markdown",
    url="https://github.com/stvoutsin/sparkMonitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
