# n <=50
n = int(input())
serial_arr = list(input() for _ in range(n))


def sum_digit(x):
    result = 0
    for value in x:
        if value.isdigit():
            result += int(value)
    return result


serial_arr.sort(key=lambda x: (len(x),
                               sum_digit(x), x))
print(*serial_arr, sep="\n")