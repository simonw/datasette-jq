from datasette import hookimpl
import pyjq
import json


def jq(value, expression):
    try:
        return json.dumps(pyjq.first(expression, json.loads(value)))
    except Exception as e:
        return json.dumps({"error": str(e)})


@hookimpl
def prepare_connection(conn):
    conn.create_function("jq", 2, jq)
