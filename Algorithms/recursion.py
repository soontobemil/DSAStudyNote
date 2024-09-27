counter = 0

def inception():
    global counter
    print(counter)
    if counter > 3:
        return 'done'
    counter +=1
    return inception()

result = inception()
print(result)
