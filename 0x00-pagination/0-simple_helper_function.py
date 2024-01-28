#!/usr/bin/env python3
"""Function named index_range that takes two integer
arguments page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function return a tuple of size two containing start and end index
    corresponding to the range of indexes to return in a list of particular
    pagination parameters
    Args:
        page(int): page number to return
        page_size(int): number of items per page
    Return: tuple(start, end)
    """

    start = 0
    end = 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
