import pytest
from algorithms.dynamic_programming.advent_of_code_2020_day_10.day_10 import Adapters


@pytest.fixture
def adapters():
    sample_input = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    adapter = Adapters(sample_input)

    return adapter


ALL_COMBOS = [
    [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22],
    [0, 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, 22],
    [0, 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, 22],
    [0, 1, 4, 5, 7, 10, 12, 15, 16, 19, 22],
    [0, 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, 22],
    [0, 1, 4, 6, 7, 10, 12, 15, 16, 19, 22],
    [0, 1, 4, 7, 10, 11, 12, 15, 16, 19, 22],
    [0, 1, 4, 7, 10, 12, 15, 16, 19, 22],
]


def test_connection_graph(adapters):
    expected = {
        0: [1],
        1: [4],
        4: [5, 6, 7],
        5: [6, 7],
        6: [7],
        7: [10],
        10: [11, 12],
        11: [12],
        12: [15],
        15: [16],
        16: [19],
        19: [22],
    }

    actual = adapters.connection_graph

    assert actual == expected


@pytest.mark.parametrize(
    "adapter_values,expected",
    [([0, 1], 1), ([4, 5, 6], 2), ([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22], 8)],
)
def test_path_count(adapter_values, expected):
    adapters = Adapters(adapter_values)
    first, *_, last = adapter_values

    actual = adapters.path_count(first, last)

    assert actual == expected


@pytest.mark.benchmark(group="advent-of-code")
def test_path_count_performance(benchmark, adapters):
    expected = 8

    actual = benchmark(adapters.path_count, 0, 22)

    assert actual == expected


@pytest.mark.benchmark(group="advent-of-code")
def test_dynamic_programming_path_count_preformance(benchmark, adapters):
    expected = 8

    actual = benchmark(adapters.path_count_dp, 0, 22)

    assert actual == expected


# def test_configurations(adapters):
#     expected = ALL_COMBOS

#     actual = adapters.valid_configurations

#     assert actual == expected


# def test_configuration_count(adapters):
#     expected = 8

#     actual = adapters.count_configurations()

#     assert actual == expected
