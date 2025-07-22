def decor(func):
    def inner():
        print("**********")
        func()
        print("**********")
    return inner
@decor
def msg():
    print("Calculator!")
msg()
def opt():
    while True:
        print("\nSelect the Operation!")
        print("Addition = '+'")
        print("Subtraction = '-'")
        print("Multiplication = '*'")
        print("Divide = '/'")
        print("Exit = 'E'")
        num1=int(input("Enter the First number: "))
        num2=int(input("Enter the Second number: "))
        ope=str(input("Enter the Operation: "))
        if ope=='+':
            print("Result:",num1+num2)
        elif ope=='-':
            print("Result:",num1-num2)
        elif ope=='*':
            print("Result:",num1*num2)
        elif ope=='/':
            print("Result:",num1/num2)
        elif ope=='e' or ope=='E':
            print("Good Bye!")
            break
        else:
            print("Invalide Operation!")
            break
opt()
