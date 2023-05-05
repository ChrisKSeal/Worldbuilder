# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,protected-access
import pytest

from src.common.random import DiceRoller


@pytest.fixture
def dice():
    return DiceRoller(seed=123456789)


@pytest.mark.parametrize(
    "test_value, expected_value",
    (
        ("1D4", [((1, 4, 0, None, None), None)]),
        ("2d6", [((2, 6, 0, None, None), None)]),
        ("d8r3", [((1, 8, 0, None, "r3"), None)]),
        ("d10+3", [((1, 10, 3, "+", None), None)]),
        ("d12-2", [((1, 12, 2, "-", None), None)]),
        ("d20*3", [((1, 20, 3, "*", None), None)]),
        ("d20x3", [((1, 20, 3, "x", None), None)]),
        ("d100 / 5", [((1, 100, 5, "/", None), None)]),
        ("d4+d6", [((1, 4, 0, None, None), "+"), ((1, 6, 0, None, None), None)]),
        ("d4+3 - 2d6/2", [((1, 4, 3, "+", None), "-"), ((2, 6, 2, "/", None), None)]),
        ("2d2r3/2-d6", [((2, 2, 2, "/", "r3"), "-"), ((1, 6, 0, None, None), None)]),
    ),
)
def test_string_parser(test_value, expected_value, dice):
    assert dice._DiceRoller__parse_dice_string(test_value) == expected_value


@pytest.mark.parametrize(
    "test_value, expected_value",
    (
        ((1, 4, 0, None, None), 4),
        ((2, 6, 0, None, None), 10),
        ((1, 8, 1, "+", None), 9),
        ((1, 10, 4, "-", None), 4),
        ((1, 12, 2, "*", None), 22),
        ((2, 20, 2, "/", None), 16.5),
    ),
)
def test_parse_dice_tuple(test_value, expected_value, dice):
    assert dice._DiceRoller__parse_dice_tuple(test_value) == expected_value


@pytest.mark.parametrize(
    "test_value, expected_value",
    (
        ("1d4", 4),
        ("2d6", 10),
        ("1d8+1", 9),
        ("1d10-4", 4),
        ("1d12*2", 22),
        ("1d12x2", 22),
        ("2d20/2", 16.5),
    ),
)
def test_roll(test_value, expected_value, dice):
    """Given we are reseeding the DiceRoller with the same seed, the expected values are
    consistent for testing purposes."""
    assert dice.roll(test_value) == expected_value  # nosec
