var = 1
check3 = var % 3
check5 = var % 5


if check3 == 0 and check5 == 0:
    print("FizzBuzz")
elif check3 == 0:
    print("Fizz")
elif check5 == 0:
    print("Buzz")
else:
    print(var)