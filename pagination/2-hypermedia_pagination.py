#!/usr/bin/env python3#!/usr/bin/env python3

""" function named index_range takes two integer arguments page and page_size

    Page numbers are 1-indexed, i.e. the first page is page 1 """

from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Implement a method named get_page that takes two integer arguments
            page with default value 1 and page_size with default value 10 """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = Server.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """ return tuple of size two containing a start index and an end index
            corresponding to the range of indexes to return in a list for those
            particular pagination parameters """
        return ((page - 1) * page_size, page * page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Implement a method named get_hyper that takes the same arguments
            (and defaults) as get_page and returns a dictionary containing
            the following key-value pairs """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
