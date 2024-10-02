#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    returns pascals triangle
    """
    triangle = [[1]]
    if n <= 0:
        return print([])
    for i in range(n - 1):
        new_row = []
        curr_row = triangle[i]
        for j in range(len(curr_row)):
            if j == 0:
                new_row.append(1)
            if j + 1 == len(curr_row):
                new_row.append(1)
            else:
                new_row.append(curr_row[j] + curr_row[j + 1])
        triangle.append(new_row)
    return triangle
