def square(number):
  if not (number > 0 and number < 65):
    raise ValueError('square must be between 1 and 64')

  return 2**(number-1)


def total():
  suma = 0
  for i in range(1, 65):
    suma = suma + square(i)
    print(square(i))
  return suma

print(square(1))
print(square(2))
print(square(3))
print(square(4))
print(square(5))
print(square(6))

total()

