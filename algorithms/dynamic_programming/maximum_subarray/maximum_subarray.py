def maximum_subarray(items: list) -> list:
    max_subarray = []

    item_count = len(items)
    for start in range(item_count):
        for end in range(start + 1, item_count + 1):
            subarray = items[start:end]
            if sum(subarray) >= sum(max_subarray):
                max_subarray = subarray

    return max_subarray


def maxium_subarray_sum(items: list) -> int:
    return sum(maximum_subarray(items))


def dynamic_programming_maximum_subarray(items: list) -> list:
    """
    Sub problem: the rolling subarray maximum.

    Memo-ise: the max_end so that we can work back from the biggest to
    the most recent non-negative value.
    """
    max_end = 0
    max_ends = []
    for index, item in enumerate(items):
        max_end = max(item, item + max_end)
        max_ends.append(max_end)

    if not max_ends:
        return []

    max_val = max(max_ends)
    max_index = max_ends.index(max_val)
    for i in range(max_index, 0, -1):
        if max_ends[i] < 0:
            return items[i + 1 : max_index + 1]

    return items[: max_index + 1]


def dynamic_programming_maximum_subarray_sum(items: list) -> list:
    max_seen = max_end = 0
    for item in items:
        max_end = max(item, item + max_end)
        max_seen = max(max_seen, max_end)

    return max_seen
