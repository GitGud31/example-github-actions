def average(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)


def get_minimum(values):
    if len(values) == 0:
        return None
    return min(values)
