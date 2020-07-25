import sys

def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        root = arr[0]
        less = [i for i in arr[1:] if i <= root]
        greater = [i for i in arr[1:] if i > root]
        return qsort(less) + [root] + qsort(greater)

           
        

arr = list(map(lambda x: float(x), sys.argv[1].split(',')))
print(qsort(arr))