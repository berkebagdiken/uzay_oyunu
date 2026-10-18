# Ad Soyad: Berke Bağdiken
# Hafta 4 - Akış ve Üreteç Modülü

from collections.abc import Generator
import functools
import itertools
from pathlib import Path
from typing import Any, Callable


def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayı dizisi üreten üreteç (0, 1, 1, 2, 3, 5, ...)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b