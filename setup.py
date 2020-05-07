import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyr",
    version="0.1.0",
    author="Knut Magnus Aasrud",
    author_email="kmaasrud@outlook.com",
    description="Python weather API, supported by data from yr.no",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmaasrud/pyr",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)