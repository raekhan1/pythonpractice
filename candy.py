def hcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
        # Question: why doesn't
        # num1 = num2
        # num2 = num1% num2
        # work
    return num1


def candy(first_list):
    total = 0

    if len(first_list) == 1:
        gcd = first_list[0]

    else:
        gcd = first_list[0]
        for i in first_list:
            gcd = hcf(gcd, i)

    for i in range(0, len(first_list)):
        total = int(total + first_list[i]/gcd)

    return gcd, total

print(candy([3,6,9]))
