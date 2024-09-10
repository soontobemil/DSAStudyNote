def HaveCommonArray(Array1, Array2):
    common_elements = []
    for i in range(len(Array1)):
        for j in range(len(Array2)):
            if Array1[i] == Array2[j]:
                common_elements.append(Array1[i])
                print(common_elements)
    return False

example1 = ['a','b','c','d']
example2 = ['z','x','y','d']

# Print the result of the function call
print(HaveCommonArray(example1, example2))
