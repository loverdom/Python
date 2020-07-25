def binary_search(list, target):
    list.sort()
    low, high = 0, (len(list) - 1)
    while low <= high:
        temp = (low + high) // 2
        if target == list[temp]:
            print(temp)
            break
        elif target < list[temp]:
            high = temp - 1
            continue
        elif target > list[temp]:
            low = temp + 1
            continue
