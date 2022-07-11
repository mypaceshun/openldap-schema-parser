from pathlib import Path

import pytest

from openldap_schema_parser.parser import parse
from openldap_schema_parser.schema import Schema

BASE_DIR = Path(__file__).parent
SCHEMA_DIR = Path(BASE_DIR, "schema")

TEST_SCHEMA_FILES = [(p) for p in SCHEMA_DIR.glob("*.schema")]


@pytest.mark.parametrize("target_file", TEST_SCHEMA_FILES)
def test_parse(target_file):
    result = parse(target_file)
    repr(result)
    assert isinstance(result, Schema)
