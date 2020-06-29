def add(array, item):
    array.append(item) 
    return array


def reverse(array):
    array.reverse()
    return array


def five_index(array):
    index = 0
    for ind, x in enumerate(array):
        print(ind, x)
        if x == 5:
            print(ind)
            index = ind
            break
    return index

def add_before_second(array, item):
    array.insert(1, item)
    return array


def remove_duplicates(array):
    a = []
    for x in array:
        if x not in a:
            a.append(x)
    return a

