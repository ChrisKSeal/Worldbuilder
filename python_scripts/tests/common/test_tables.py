# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,protected-access
from typing import Dict, List

import pytest

from python_scripts.src.common.tables import Table


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
    ),
)
def test_parse_input(
    test_value: List[str],
    expected_value: Dict[int, str],
) -> None:
    assert Table.parse_input(test_value) == expected_value
