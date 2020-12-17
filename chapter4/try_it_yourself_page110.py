numbers = list(range(0,21))
print(numbers)


numbers1 = list(range(0,1000001))
print(numbers1)

print(min(numbers1))

print(max(numbers1))

print(sum(numbers1))


odd_numbers = list(range(0,50,5))
print(odd_numbers)


squares = []
for value in range(3,30):
 square = value **3
 square.append(square)
 print(squares)