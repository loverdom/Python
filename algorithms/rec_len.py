import sys

def rec_len(arr, count):
    while arr != []:
        arr.pop(0)
        count += 1
        rec_len
    return count    

arr = sys.argv[1].split(',')
print(rec_len(arr, 0))           