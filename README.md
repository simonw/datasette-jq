# datasette-jq

[![PyPI](https://img.shields.io/pypi/v/datasette-jq.svg)](https://pypi.org/project/datasette-jq/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-jq.svg?style=svg)](https://circleci.com/gh/simonw/datasette-jq)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-jq/blob/master/LICENSE)

Datasette plugin that adds custom SQL functions for executing [jq](https://stedolan.github.io/jq/) expressions against JSON values.

Install this plugin in the same environment as Datasette to enable the `jq()` SQL function.

Usage:

    select jq(
        column_with_json,
        "{top_3: .classifiers[:3], v: .version}"
    )

See [the jq manual](https://stedolan.github.io/jq/manual/#Basicfilters) for full details of supported expression syntax.
