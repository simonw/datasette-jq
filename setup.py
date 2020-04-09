from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-jq",
    description="Datasette plugin that adds custom SQL functions for executing jq expressions against JSON values",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-jq",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_jq"],
    entry_points={"datasette": ["jq = datasette_jq"]},
    install_requires=["datasette", "pyjq", "six"],
    extras_require={
        "test": [
            "pytest"
        ]
    },
    tests_require=["datasette-jq[test]"],
)
