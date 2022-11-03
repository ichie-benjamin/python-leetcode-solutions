def num_to_time(num):
    intervals = (
        ('w', 604800),  # 60 * 60 * 24 * 7
        ('d', 86400),  # 60 * 60 * 24
        ('h', 3600),  # 60 * 60
        ('m', 60),
        ('s', 1),
    )
    result = []

    for name, count in intervals:
        value = num // count
        if value:
            num -= value * count
            result.append("{}{}".format(value, name))

    if len(result) == 3:
        result[1] = str(int(result[1].rsplit('m')[0])+1)+'m'
    return ''.join(result[:2])


print(num_to_time(7263))
