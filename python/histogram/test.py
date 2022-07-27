from operator import length_hint


def get_histogram(bin_count: int, max_value: int, measurements: list) -> dict:

    step = max_value // bin_count
    bins = [i + step for i in range(0, max_value, step)]

    histogram = {}
    for bin_max_value in bins:
        histogram[bin_max_value] = len([i for i in measurements if i <= bin_max_value])

    result = {
        "total": sum(measurements),
        "count": len(measurements),
        "histogram": histogram,
    }

    return result


if __name__ == "__main__":
    print(get_histogram(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(get_histogram(5, 10, [1, 2, 8, 9, 9, 9, 9, 10, 10, 10]))
