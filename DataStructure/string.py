
def reverse_string(s):
    if not isinstance(s, str) or len(s) < 2:
        print("it's not a correct string")
        return False
    text = s[::-1]
    return text

print(reverse_string(input()))
