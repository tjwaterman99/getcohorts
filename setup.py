import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getcohorts",
    version="1.0.0",
    author="Tom Waterman",
    author_email="tjwaterman99@gmail.com",
    description="Utilities for randomizing A/B tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'gunicorn==20.0.4',
        'fastapi==0.61.1',
        'uvicorn==0.11.8',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    url="http://docs.getcohorts.com/"
)
