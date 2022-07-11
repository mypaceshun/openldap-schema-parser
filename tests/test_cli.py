from pathlib import Path

import pytest
from click.testing import CliRunner

from openldap_schema_parser.command import cli

BASE_DIR = Path(__file__).parent
SCHEMA_DIR = Path(BASE_DIR, "schema")


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "target",
    [
        ("basic_attribute.schema"),
        ("basic_objectclass.schema"),
        ("test_expand_oid.schema"),
    ],
)
def test_cli_parse(target):
    target_file = Path(SCHEMA_DIR, target)
    runner = CliRunner()
    result = runner.invoke(cli, [str(target_file), "--expand-oid"])
    assert result.exit_code == 0
