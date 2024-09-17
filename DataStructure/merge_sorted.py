def merge_sorted_array(arr1, arr2):
    # Check inputs
    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    else:
        arr3 = arr1 + arr2
        arr3.sort()
        return arr3

arr1 = [0,3,4,31]
arr2 = [4,6,30]

print(merge_sorted_array(arr1,arr2))
