import requests
import sqlite_utils

packages = (
    "datasette-jq",
    "datasette-cluster-map",
    "datasette-vega",
    "datasette-jellyfish",
    "datasette-pretty-json",
    "datasette-json-html",
)


def make_demo():
    table = sqlite_utils.Database("demo.db")["packages"]
    to_insert = []
    for package in packages:
        info = requests.get("https://pypi.org/pypi/{}/json".format(package)).json()
        to_insert.append({"package": package, "info": info})
    table.insert_all(to_insert, pk="package")


if __name__ == "__main__":
    make_demo()
