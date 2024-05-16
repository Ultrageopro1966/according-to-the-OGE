"""Мммм... информатика..."""


def main() -> None:
    """Solve the problem."""
    counter1 = 0  # number of 3-digit numbers
    counter2 = 0  # number of multiples of 4
    counter3 = 0  # number ofnumbers ending in 3

    while True:  # endless loop
        n = int(input())  # read a number

        if not n:  # break if n == 0
            break

        if len(str(abs(n))) == 3:  # 3-digit numbers  # noqa: PLR2004
            counter1 += 1

        if n % 4 == 0:  # multiples of 4
            counter2 += 1

        if abs(n) % 10 == 3:  # numbers ending in 3  # noqa: PLR2004
            counter3 += 1

    # print results
    print(counter1, counter2, counter3, sep="\n")  # noqa: T201


# call the main function
if __name__ == "__main__":
    main()  # main function
