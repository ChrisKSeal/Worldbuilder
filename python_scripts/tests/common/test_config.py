# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,protected-access

import logging
from unittest.mock import patch

import pytest
import tomlkit

from python_scripts.src.common.config import WorldBuilderConfig


@pytest.fixture
def log_file():
    return "worldbuilder.log"


@pytest.fixture
def log_level():
    return "DEBUG"


@pytest.fixture
def config_from_toml(log_file, log_level) -> str:
    return tomlkit.dumps(
        {
            "logging": {
                "level": log_level,
                "filename": log_file,
            },
        }
    )


@patch("pathlib.Path.exists")
@patch("toml.load")
def test_config(
    mock_toml,
    mock_exists,
    log_file,
    log_level,
    config_from_toml,
) -> None:
    mock_toml.return_value = tomlkit.loads(config_from_toml)
    mock_exists.return_value = True
    config = WorldBuilderConfig()
    assert config.logging.level == log_level
    assert config.logging.filename == log_file
