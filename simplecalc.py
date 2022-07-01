addition = ['Add', 'Addition', 'add', 'addition']
substract = ['Substract', 'substract', 'substraction']
multiply = ['Multiply', 'multiply', 'multiplication']
division = ['Divide', 'divide', 'division']
square = ['square', 'Square', 'square', 'root']

running = False 
options = True
#Asks for Choice of Calculation
while options:
    choice = input("Do you want to Add/Substract/Multiply/Divide/Square?")
    if choice not in addition and choice not in substract and choice not in multiply and choice not in division and choice not in square:
        print("{} is not an option".format(choice))
        options = False
    else: 
        print("You Chose {}".format(choice.title()))
        running = True
        options = False

while running:
    #Asks for Numbers, Only 2 For Now
    num1 = float(input("Enter number 1 here:  "))
    num2 = float(input("Enter number 2 here:  "))

    #Calculations:
    if choice in addition:
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
        running = False
    elif choice in substract:
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
        running = False
    elif choice in multiply:
        result = num1*num2
        print("{} x {} = {}".format(num1, num2, result))
        running = False
    elif choice in division:
        result = num1/num2
        print("{} / {} = {}".format(num1, num2, result))
        running = False
    elif choice in square:
        result = num1 ** num2
        print("{} ^ {} = {}".format(num1, num2, result))
        running = False
    else: 
        print("{} is not an option".format(choice))
        running = False