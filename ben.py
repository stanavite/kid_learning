numbers = [1,1,2,3,4]
first = set(numbers)
second ={1,5}

print(first)
print(second)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

print(numbers[0])
if 1 in first:
    print("yes")
