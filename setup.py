from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

install_requires = ["numpy"]

setup(
	name="pystoch",
	version="0.0.4",
	author="Dimitry Galkin and Dmitry Bogod",
	author_email="dimgal2011@gmail.com",
	description="Python package for modeling stochastic processes and for SDE analysis",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/PyPaperParrot/pystoch",
	packages=find_packages(),
    	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	],
	install_requires=install_requires,
	setup_requires=["numpy"],
)
