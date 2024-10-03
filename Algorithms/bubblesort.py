numbers = [1,5,6,34,52,3,55,362]

def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
               tmp = array[j]
               array[j] = array[j+1]
               array[j+1] = tmp
    return array

print(bubbleSort(numbers))

