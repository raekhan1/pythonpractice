def di_sum(n):

    total = 0
    while n >= 1:
        total += (n % 10)
        n = n // 10
    return total

def tickets(n,_sum):

    count = n * len(str(_sum))

    total = []

    while len(str(count)) < n+1:
        if di_sum(count) == _sum:
            total.append(count)
        count = count + 1

    return len(total), total


print(tickets(6, 50))
