def grid_land(_list, i=0, f=0, empty_list=[], adj_m=[]):
    if i < len(_list):

        while f < len(_list):

            x_value = _list[i] - _list[f]
            y_value = _list[i + 1] - _list[f + 1]

            if x_value < 0:
                x_value = int(x_value / -1)

            if y_value < 0:
                y_value = int(y_value / -1)

            weight = x_value + y_value

            if weight == 0:
                empty_list.append(-1)

            else:
                empty_list.append(weight)
            f = f + 2


        adj_m.append(empty_list)
        grid_land(_list, i + 2, 0, [], adj_m)

    else:
        graph(adj_m)



def graph(adj_m):

    print(adj_m)
    ticked = [0]
    total = 0

    # going through the visited columns
    for column in range(0, len(adj_m) - 1):

        min_val = 99999


        # if the column is not ticked skip column

        if column not in ticked:
            continue

        # going through each ticked column
        row = 0
        for y in adj_m[column]:

            # finding min value and its row
            if row in ticked:
                row += 1
                continue

            if 0 < y < min_val:
                min_val = y
                del_row = row
            row += 1

        ticked.append(del_row)
        total = total + min_val

    print(total)



grid_land([3, 6, 7, 9, 4, 4, 1, 7, 8, 2])
