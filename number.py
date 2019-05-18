numbers = [3,5,7,9,10.5]
numbers.append('Python')
print(numbers)
print(len(numbers))
print(numbers[:1])
print(numbers[-1])
print(numbers[1:4])
numbers.remove('Python')
print(numbers)
del numbers[-1]
print(numbers)