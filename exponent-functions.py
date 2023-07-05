# Allows us to take a specific number and raise it to a specific power


def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print(raise_to_power())
