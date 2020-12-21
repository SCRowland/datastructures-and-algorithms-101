import pytest
from algorithms.dynamic_programming.fibonacci import (
    cached_recursive_fibonacci,
    dynamic_programming_fibonacci,
    recursive_fibonacci,
)

FIBONACCI_SEQUENCE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
]


@pytest.mark.parametrize(
    "input_,expected",
    FIBONACCI_SEQUENCE,
)
def test_recursive_fibonacci_correctness(input_: int, expected: int) -> None:
    actual = recursive_fibonacci(input_)

    assert actual == expected


def test_recursive_fibonacci_flags_recursion_limit():
    with pytest.raises(ValueError) as exc:
        recursive_fibonacci(10000)


def test_recursive_fibonacci_performance(benchmark) -> None:
    expected = 75025

    result = benchmark(recursive_fibonacci, 25)

    assert result == expected


@pytest.mark.parametrize(
    "input_,expected",
    FIBONACCI_SEQUENCE,
)
def test_cached_recursive_fibonacci_correctness(input_: int, expected: int) -> None:
    actual = cached_recursive_fibonacci(input_)

    assert actual == expected


def test_cached_recursive_fibonacci_performance(benchmark) -> None:
    expected = 75025

    result = benchmark(cached_recursive_fibonacci, 25)

    assert result == expected


@pytest.mark.parametrize(
    "input_,expected",
    FIBONACCI_SEQUENCE,
)
def test_dynamic_programming_fibonacci_correctness(input_: int, expected: int) -> None:
    actual = dynamic_programming_fibonacci(input_)

    assert actual == expected


def test_dynamic_programming_fibonacci_performance(benchmark) -> None:
    expected = 75025

    result = benchmark(dynamic_programming_fibonacci, 25)

    assert result == expected
