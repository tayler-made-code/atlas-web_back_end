#!/usr/bin/env python3

""" function named index_range takes two integer arguments page and page_size

    Page numbers are 1-indexed, i.e. the first page is page 1 """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters """
    return ((page - 1) * page_size, page * page_size)
