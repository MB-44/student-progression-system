def factorial(num):
    if num < 0:
        return "you entered a negative number"
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i
    return fact

num = int(input("Enter a positive number: "))
x = factorial(num)
print(x)

