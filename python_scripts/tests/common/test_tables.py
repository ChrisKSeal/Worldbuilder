# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,protected-access
# pylint: disable=unused-argument,protected-access
import json
from pathlib import Path
from typing import Dict, List

import pytest

from python_scripts.src.common.tables import Table, read_json_files


@pytest.fixture
def read_simple_json() -> str:
    return json.dumps(
        {
            "test_table": {
                "name": "Test Table",
                "data": [
                    "value1",
                    "value2",
                    "value3",
                    "value4",
                    "value5",
                ],
                "min_roll": 1,
                "max_roll": 5,
            }
        }
    )


@pytest.fixture
def table_from_simple_json() -> Table:
    return Table(
        name="Test Table",
        data=[
            "value1",
            "value2",
            "value3",
            "value4",
            "value5",
        ],
        max_roll=5,
        min_roll=1,
    )


@pytest.fixture
def mocker_simple_json(mocker, read_simple_json) -> None:  # type: ignore[no-untyped-def]
    # Read a mocked /etc/release file
    mocked_yaml_data = mocker.mock_open(read_data=read_simple_json)
    mocker.patch("builtins.open", mocked_yaml_data)


@pytest.mark.parametrize(
    "test_value, expected_value",
    (
        (["Test"], {1: "Test"}),
        (["23, Test"], {23: "Test"}),
        (
            ["13-17, Test"],
            {
                13: "Test",
                14: "Test",
                15: "Test",
                16: "Test",
                17: "Test",
            },
        ),
        (
            [
                "value1",
                "value2",
                "value3",
                "value4",
                "value5",
            ],
            {
                1: "value1",
                2: "value2",
                3: "value3",
                4: "value4",
                5: "value5",
            },
        ),
    ),
)
def test_parse_input(
    test_value: List[str],
    expected_value: Dict[int, str],
) -> None:
    assert Table.parse_input(test_value) == expected_value


def test_table_equal(table_from_simple_json) -> None:  # type: ignore[no-untyped-def]
    new_table = Table(
        name="Test Table",
        data=[
            "value1",
            "value2",
            "value3",
            "value4",
            "value5",
        ],
        max_roll=5,
        min_roll=1,
    )
    assert new_table == table_from_simple_json


def test_check_json_file_mock(mocker_simple_json, read_simple_json):  # type: ignore[no-untyped-def]
    with open("fakefile", "r", encoding="UTF-8") as test_file:
        test_yaml_data = test_file.read()
    assert test_yaml_data == read_simple_json


def test_tbl_from_json(mocker_simple_json, table_from_simple_json):  # type: ignore[no-untyped-def]
    tables = read_json_files(Path("fakefile"))
    assert tables[0] == table_from_simple_json
