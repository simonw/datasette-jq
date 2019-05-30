from datasette_jq import prepare_connection
import sqlite3
import pytest
import json


@pytest.mark.parametrize(
    "data,jq,expected",
    (
        ({"foo": "bar"}, ".foo", '"bar"'),
        ({"foo": [1, 2, 3, 4, 5]}, ".foo[:2]", "[1, 2]"),
    ),
)
def test_jq(data, jq, expected):
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    sql = "select jq(?, ?)"
    result = conn.execute(sql, (json.dumps(data), jq)).fetchone()[0]
    assert expected == result
