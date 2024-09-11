# def HaveCommonArray(Array1, Array2):
#     common_elements = []
#     for i in range(len(Array1)):
#         for j in range(len(Array2)):
#             if Array1[i] == Array2[j]:
#                 common_elements.append(Array1[i])
#                 print(common_elements)
#     return False

# example1 = ['a','b','c','d']
# example2 = ['z','x','y','d']

# # Print the result of the function call
# HaveCommonArray(example1, example2)
# Nested Loops => O(n*2)
# Space Complexity of O(1)

arry1 = ['a','b','c','d']
arry2 = ['z','x','y','c']

def have_common_element(array1, array2):
    element_tracker = {}

    for element in array1:
        element_tracker[element] = True

    for element in array2:
        if element in element_tracker:
            return True

    return False

print(have_common_element(arry1, arry2))

# Not a nested loop
# O(a+b) Time Complexity is better
# Space Complexity of O(n)
# This is faster than the previous brute force nested loop

# How can you possibly break the code? Null, Input? etc
# Naming the variables, Not I or J ....
# Unit test
# Talk to the interviewer how you would improve the code
