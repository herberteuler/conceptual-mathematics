from itertools import product
import sys
from typing import Callable, Iterable, List


def mk_map(vs: List[int]) -> Callable[[int], int]:
    return lambda k: vs[k]


def mk_variants(n: int) -> Iterable[List[int]]:
    return map(list, product(range(n), repeat=n))


if __name__ == "__main__":
    n = int(sys.argv[1])
    total = 0
    for vs in mk_variants(n):
        f = mk_map(vs)
        ws = list(map(lambda k: f(f(k)), range(n)))
        print(f"{vs}, {ws}")
        if vs == ws:
            total += 1
    print(total)
