"""Мммм... информатика..."""

from __future__ import annotations


def main() -> None:
    """Solve the problem."""
    # read the strings
    string1: str = input()
    string2: str = input()
    string3: str = input()

    # get max length
    max_length: int = max(len(string1), len(string2), len(string3))

    # get next char after "z" letter
    next_char: str = chr(ord("z") + 1)

    # sort the strings
    sorted_data: list[str] = sorted(
        [string1, string2, string3],
        key=lambda x: x.ljust(max_length, next_char),
    )

    # print the result
    print("".join(sorted_data))


# call the main function
if __name__ == "__main__":
    main()  # main function
