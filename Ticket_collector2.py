def di_sum(count):

    total = 0
    while count >= 1:
        total += (count % 10)
        count = count // 10
    return total

def tickets(n, _sum, x= 1, grid=[]):

    if x < 5:
        count = x * len(str(_sum))

        total = []

        while len(str(count)) < x+1:
            if di_sum(count) == _sum:
                total.append(count)
            count = count + 1
        grid.append(total)
        if x == n:
            return len(grid[x-1]), grid[x]
        else:
            tickets(n,_sum,x+1,grid)
    else:
        t= 0
        total =[]

        for i in range(grid[x-2[len[grid[x-2]]]]-10, grid[x-2[len[grid[x-2]]]]):
            t = t+i
            total.append(t)
        grid.append(total)

        if x == n:
            return len(grid[x - 1]), grid[x]

        else:
            tickets(n, _sum, x+1, grid)


print(tickets(6, 50))
