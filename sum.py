def sum_f(X, B, Z):
    if sum(B) == X:
        return 0

    val = X - sum(B)
    if len(B) < Z:
        avr = sum(B) / len(B)
    else:
        avr = sum(B[-Z:]) / Z

    est = val / avr
    return est
    return int(round(est))


arr = [10, 6, 6, 8]
a = 100
zi = 2
print(sum_f(a, arr, zi))
