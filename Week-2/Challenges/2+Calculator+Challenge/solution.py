logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""
def calculate():
    print(logo)
    num1=float(input("What's the first number?: "))
    while True:
        print("+\n-\n*\n/")
        operation=input("Pick an operation: ")
        num2=float(input("What's the next number?: "))
        if operation=="+":
            solution=num1+num2
        elif operation=="-":
            solution=num1-num2
        elif operation=="*":
            solution=num1*num2
        elif operation=="/":
            if num2==0:
                print("Division by 0 is undefined")
                continue
            solution=num1/num2
        else:
            solution=0.0
        
        choice = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation: ")
        if choice=="y":
            num1=solution
            
        elif choice=="n":
            break


calculate()
