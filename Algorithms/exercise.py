def reverseString(str):
    reversed_str = ""
    for i in range(len(str) - 1, -1, -1):
        reversed_str += str[i]
    return reversed_str

print(reverseString("yoyo master"))

def reverseStringRecursive(str):
    if len(str) == 0:
        return str

    return str[-1] + reverseStringRecursive(str[:-1])


reverseStringRecursive("yoyo master")
