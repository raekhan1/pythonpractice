def queue(initial, n):

    q = []
    for i in range(0, n):
        q.append(initial)
        line = (initial*31334) % 31337
        initial = line

    find = q[n - 1]
    q.sort()

    for x in range(0, n):
        if q[x] == find:
            final = x

    return final + 1

print(queue(7546, 6))
