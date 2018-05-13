def grid_land(_list, i=0, f=0, empty_list=[], adj_m=[]):

    if i < len(_list):

        while f < len(_list):

            x_value = _list[i] - _list[f]
            y_value = _list[i+1]-_list[f+1]

            if x_value < 0:
                x_value = int(x_value / -1)

            if y_value < 0:
                y_value = int(y_value / -1)

            weight = x_value + y_value

            if weight == 0:
                empty_list.append(" ")

            else:
                empty_list.append(weight)
            f = f + 2

        adj_m.append(empty_list)
        grid_land(_list, i+2, 0, [], adj_m)

    else:
        graph(adj_m)


def graph(adj_m):

    new_list = []
    total = 0
    maxi = 100
    while len(new_list) != len(adj_m):
        counter = 0
        row = 0
        column = 0
        while column < len(new_list)-1:
            for i in range(0, 4):
                if column[i] < maxi:
                    maxi = i
                    row += 1

            column += 1
        # deleting the rows

        while counter < len(adj_m):
            adj_m[counter].remove(adj_m[counter][row])
            counter += 1

        new_list.append(adj_m[row])
        total = total + maxi
    print(total)

grid_land([3, 6, 7, 9, 4, 4, 1, 7, 8, 2])

