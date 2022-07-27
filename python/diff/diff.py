def count_absolute_differences(l, x: int) -> int:
    pairs = set()
    # pairs = set()
    for i in range(len(l) - 1):
        n1 = l[i]
        n2 = l[i + 1]
        if abs(n1 - n2) == x:
            pairs.add((n1, n2)) if n1 < n2 else pairs.add((n2, n1))

    return len(pairs)
    # return len(pairs)


if __name__ == "__main__":

    print(count_absolute_differences([5, 6, 7, 8], 1))
    print(count_absolute_differences([1, 1, 9, 8, 7], 0))
    print(count_absolute_differences([5, 2, 6, 3, 3], 3))
