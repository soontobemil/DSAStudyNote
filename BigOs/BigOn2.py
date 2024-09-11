# Log all pairs of array
# O(n*2) - Quadratic Time
# Nested Loops 

boxes = ["a",2,3,4,5]

def log_all_arrays(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

log_all_arrays(boxes)
