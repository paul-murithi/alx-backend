#!/usr/bin/env python3
""" index_range that takes two integer arguments
    page and page_size
"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index
    and an end index
    Args:
         page: pages
         Page_size: the page size
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
