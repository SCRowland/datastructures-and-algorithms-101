import sys
from collections import defaultdict
from functools import cache


def recursive_fibonacci(n: int) -> int:
    recursion_limit = sys.getrecursionlimit()

    if n > recursion_limit:
        raise ValueError(
            f"Can't recursively calculate results greater than the recursion limit ({recursion_limit})."
        )

    if n in [0, 1]:
        return n

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


@cache
def cached_recursive_fibonacci(n: int) -> int:
    """
    Uses caching to memo-ise results as it goes. Has the benefit of
    persisting the cache across function calls
    """
    if n in [0, 1]:
        return n

    return cached_recursive_fibonacci(n - 1) + cached_recursive_fibonacci(n - 2)


def dynamic_programming_fibonacci(n: int) -> int:
    """
    Uses memo-isation to calculate sub-results as it goes
    """
    if n in [0, 1]:
        return n

    memo = defaultdict(lambda: 0)

    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
