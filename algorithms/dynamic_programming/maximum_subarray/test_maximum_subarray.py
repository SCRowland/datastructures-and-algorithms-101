import pytest
from algorithms.dynamic_programming.maximum_subarray import (
    dynamic_programming_maximum_subarray,
    dynamic_programming_maximum_subarray_sum,
    maximum_subarray,
    maxium_subarray_sum,
)


@pytest.fixture
def example_array():
    return [904, 40, 523, 12, -335, -385, -124, 481, -31]


SIMPLE_SOLUTIONS = (
    "array,subarray,sum_",
    [
        ([], [], 0),
        ([0], [0], 0),
        ([1], [1], 1),
        ([1, -1], [1], 1),
        ([1, 2, 3, 4], [1, 2, 3, 4], 10),
        ([1, 2, -5, 3, 4, -10], [3, 4], 7),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1], 6),
        ([-2, 3, 1, -7, 3, 2, -1], [3, 2], 5),
        ([904, 40, 523, 12, -335, -385, -124, 481, -31], [904, 40, 523, 12], 1479),
    ],
)


@pytest.mark.parametrize(*SIMPLE_SOLUTIONS)
def test_maximum_subarray(array, subarray, sum_):
    expected = subarray

    actual = maximum_subarray(array)

    assert actual == expected


@pytest.mark.parametrize(*SIMPLE_SOLUTIONS)
def test_maxium_subarray_sum(array, subarray, sum_):
    expected = sum_

    actual = maxium_subarray_sum(array)

    assert actual == expected


@pytest.mark.benchmark(group="maximum-subarray")
def test_maximum_subarray_performance(benchmark, example_array):
    expected = [904, 40, 523, 12]

    actual = benchmark(maximum_subarray, example_array)

    assert actual == expected


@pytest.mark.parametrize(*SIMPLE_SOLUTIONS)
def test_dynamic_programming_maximum_subarray_sum(array, subarray, sum_):
    expected = sum_

    actual = dynamic_programming_maximum_subarray_sum(array)

    assert actual == expected


@pytest.mark.parametrize(*SIMPLE_SOLUTIONS)
def test_dynamic_programming_maximum_subarray(array, subarray, sum_):
    expected = subarray

    actual = dynamic_programming_maximum_subarray(array)

    assert actual == expected


@pytest.mark.benchmark(group="maximum-subarray")
def test_dynamic_programming_maximum_subarray_performance(benchmark, example_array):
    expected = [904, 40, 523, 12]

    actual = benchmark(dynamic_programming_maximum_subarray, example_array)

    assert actual == expected
