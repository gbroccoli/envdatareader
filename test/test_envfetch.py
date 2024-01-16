import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))
from envdatareader import EnvDataReader  # noqa: E402


@pytest.fixture
def env_fetch():
    return EnvDataReader(file_path=".env")


def test_get_value_existing_key_with_value(env_fetch):
    env_fetch.variables = {"KEY": "VALUE"}
    assert env_fetch.get_value("KEY") == "VALUE"


def test_get_value_existing_key_with_default(env_fetch):
    env_fetch.variables = {"KEY": "VALUE"}
    assert env_fetch.get_value("KEY", default="DEFAULT") == "VALUE"


def test_get_value_empty_value_with_default(env_fetch):
    env_fetch.variables = {"KEY": ""}
    assert env_fetch.get_value("KEY", default="DEFAULT") == "DEFAULT"


def test_get_value_nonexistent_key_with_default(env_fetch):
    env_fetch.variables = {"EXISTING_KEY": "VALUE"}
    assert env_fetch.get_value(
        "NONEXISTENT_KEY", default="DEFAULT") == "DEFAULT"


def test_get_value_no_default(env_fetch):
    env_fetch.variables = {}
    assert env_fetch.get_value("KEY") is None
