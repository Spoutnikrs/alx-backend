#!/usr/bin/env python3
"""
Module to define function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start/end index corresponding to the range of indexes
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
