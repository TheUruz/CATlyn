from setuptools import setup, find_packages

VERSION = "0.0.1"
URL = "https://github.com/TheUruz/CATlyn"

setup(
    author="TheUruz",
    name="catlyn",
    description="A wrapper around Riot API",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    url=URL,
    license="MIT"
)
