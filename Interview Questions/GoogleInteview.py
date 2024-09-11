# pair_1 = [1,2,4,5]
# pair_2 = [1,2,4,4]
# target_sum = 8

# def pair_sum(array, target_sum):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == target_sum:
#                 return True
#     return False

# print(pair_sum(pair_2, target_sum))

def pair_exist(array, target_sum):
    seen_numbers = set() # unordered list, no duplicates

    for num in array: # for every number in array
        complement = target_sum - num  # 8 - 2 = 6 (complement)
        if complement in seen_numbers: # complement(6) in seen_numbers set?
            return True # True - because 2 and 6 are pairs matching target sum
        seen_numbers.add(num) # if not, we add number of the array let's say 5 to the seen_numbers set

    return False # When finished through an array, if there's nothing then False

pair_2 = [1, 2, 4, 3]
target_sum = 8
print(pair_exist(pair_2, target_sum))  # Output: True
