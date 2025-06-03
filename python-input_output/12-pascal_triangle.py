#!/usr/bin/python3
"""
Module: 12-pascal_triangle

This module contains a function that generates Pascal’s triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
