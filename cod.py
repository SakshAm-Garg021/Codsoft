def decor(func):
    def inner():
        print("***********")
        func()
        print("***********")
    return inner
@decor
def msg():
    print("Calculator")
msg()
def outp():
    while True:
        print("\nSelect the Operation!")
        print("Addition='+'")
        print("Subtaction='-'")
        print("Multiplication='*'")
        print("Divide='/'")
        print("Exit='5'")
        num1=int(input("Enter the First number: "))
        num2=int(input("Enter the Second number: "))
        ope=str(input("Enter the operation: "))
        if ope=='+':
            print("Result:",num1+num2)
        elif ope=='-':
            print("Result:",num1-num2)
        elif ope=='*':
            print("Result:",num1*num2)
        elif ope=='/':
            print("Result:",num1/num2)
        elif ope=='5':
            print("Good Bye !!!")
            break
        else:
            print("Invalid Operation!!")
outp()