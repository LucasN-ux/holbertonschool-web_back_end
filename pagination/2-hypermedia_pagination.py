#!/usr/bin/env python3
"""Simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """Returns the appropriate page of the dataset (i.e. the correct list
        of rows)

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The appropriate page of the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        indexes = index_range(page, page_size)
        dataset = self.dataset()
        if indexes[0] >= len(dataset):
            return []
        return dataset[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing pagination information and data.
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        hyper_dict = {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return hyper_dict
