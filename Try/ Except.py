


try:
    value= 10/0
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError:
    print("burh")
except ValueError:
    print("Invalid Input")