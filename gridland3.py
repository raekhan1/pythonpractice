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
                empty_list.append(-1)

    else:
        empty_list.append(weight)
            f = f + 2

adj_m.append(empty_list)
grid_land(_list, i+2, 0, [], adj_m)

else:
    graph(adj_m)


def graph(adj_m):
    print(adj_m)
    bl = []
    deleted = [0]
    min_val = 99999
    total = 0
    
    bl.append(adj_m[0])
    
    # going through the visited columns
    for x in range(0, len(adj_m) - 1):
        
        min_val = 99999
        
        for i in bl:
            row = 0
            
            # going through each list
            for y in i:
                # if the row is in the new_list the skip value, 'deleting the row'
                if row in deleted:
                    row += 1
                    continue
                
                # finding min value and its row
                if 0 < y < min_val:
                    delete_row = row
                    min_val = y
                row += 1
    
    deleted.append(delete_row)
        total = total + min_val
        
        if len(bl) != len(adj_m):
            bl.append(adj_m[delete_row])
    print(total)


grid_land([3, 6, 7, 9, 4, 4, 1, 7, 8, 2])

