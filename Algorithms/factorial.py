def findFactorialRecrusive(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * findFactorialRecrusive(number - 1)

def findFactorialIterative(number):
    answer = 1 # initilize the value with 1
    for i in range(1, number + 1): # for i in range, from 1 to 5 (if the input is 5)
        answer *= i # multipy the answer with i
    return answer #return the answer from the multiplication above

print(findFactorialIterative(5))
