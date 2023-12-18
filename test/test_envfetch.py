from unittest.mock import patch
import pytest
from envfetch import EnvFetch

@pytest.fixture
def env_fetch():
    return EnvFetch(file_path=".env")

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
    assert env_fetch.get_value("NONEXISTENT_KEY", default="DEFAULT") == "DEFAULT"

def test_get_value_no_default(env_fetch):
    env_fetch.variables = {}
    assert env_fetch.get_value("KEY") is None
