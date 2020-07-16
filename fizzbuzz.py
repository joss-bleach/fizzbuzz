def fizzbuzz(min, max, fizz, buzz):
    for i in range(min, max):
        if i % fizz == 0 and i % buzz == 0:
            print("fizzbuzz")
        elif i % fizz == 0:
            print("fizz")
        elif i % buzz == 0:
            print("buzz")
        else:
            print(i)
        i = i + 1


fizzbuzz(1, 100, 7, 4)
