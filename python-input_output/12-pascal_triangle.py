#!/usr/bin/python3
"""Pascal triangle generator."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            row = [1]

            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])

            row.append(1)
            triangle.append(row)

    return triangle
