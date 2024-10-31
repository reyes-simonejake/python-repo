while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the seconf number: "))
    choice = input('Enter your prefered operator + , - , * , / :  ')
    sum = num1 + num2
    diff = num1 - num2
    quitent = num1 / num2
    product = num1 * num2

    def calcu():
        if choice  == '+':
            result = num1 + num2 
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            result = num1 / num2
        print(result)

    calcu()
    calculation = input('Do you want to perform another calculation ? y/n: ')
    if calculation != 'y':
        break

