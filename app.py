"""Мммм... информатика..."""

from __future__ import annotations

import logging
from itertools import permutations
from typing import Iterator


def main() -> str:
    """Solve the problem."""
    x1, y1, z1 = int(input()), int(input()), int(input())  # sides of the first box
    x2, y2, z2 = int(input()), int(input()), int(input())  # sides of the second box

    first_box_combinations: Iterator = permutations([x1, y1, z1])

    if sorted([x1, y1, z1]) == sorted([x2, y2, z2]):
        return "Equal"

    for x, y, z in first_box_combinations:
        if (x <= x2) and (y <= y2) and (z <= z2):
            return "First"
        if (x >= x2) and (y >= y2) and (z >= z2):
            return "Second"
    return "None"


# call the main function
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # set logging config

    logging.info("App started.")
    result = main()  # main function
    logging.info("Result: %s", result)
    logging.info("App finished.")
