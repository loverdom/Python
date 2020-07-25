import sys

def rec_len(arr):
    if arr == []:
        return 0
    else:
        arr.pop(0)
        return 1 + rec_len(arr)

arr = sys.argv[1].split(',')
print(rec_len(arr))           