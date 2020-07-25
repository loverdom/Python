import sys

def rec_sum(arr):
    print(arr)
    if arr == []:
        return 0
    else:
        return arr.pop(0)+rec_sum(arr)
        

arr = list(map(lambda x: float(x), sys.argv[1].split(',')))
print(rec_sum(arr))


