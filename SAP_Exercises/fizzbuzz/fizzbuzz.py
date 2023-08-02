# add your code here
statement1 = "Fizz"
statement2 = "Buzz"

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print(statement1 + statement2)

    elif(number % 3 == 0):
        print(statement1)

    elif(number % 5 == 0):
        print(statement2)

    else:
        print(number)