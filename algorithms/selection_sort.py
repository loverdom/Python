def find_smallest(array):
    smallest, smallest_index = array[0], 0
    for el in range(len(array)):
        if smallest > array[el]:
            smallest = array[el]
            smallest_index = el
    return smallest_index    

def selection_sort(array):
    sort_array = []
    while len(array) != 0:
        smallest_index = find_smallest(array)
        sort_array.append(array.pop(smallest_index))

    return sort_array 

