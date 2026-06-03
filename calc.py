result=None
history = []
def save(op, x, y, result):
    history.append(f"{x} {op} {y} = {result} ")
    print(result)

while True:
    if result is not None:
        x = result
    else:
        try:
            x = float(input("Enter first number: "))
        except ValueError:
            print("Please enter a valid number")
            continue
    opr=input("enter operator")
    try:
            y= float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if opr == "+":
        result=x+y
        save("+",x,y,result)
    elif opr == "-":
        result=x-y
        save("-",x,y,result)
    elif opr == "*":
        result=x*y
        save("*",x,y,result)
    elif opr == "**":
        result=x**y
        save("**",x,y,result)
    elif opr == "//":
        if y == 0:
            print("Cannot divide by zero")
            continue
        else:
            result=x//y
            save("//",x,y,result)
    elif opr == "%":
        if y == 0:
            print("Cannot mod by zero")
            continue
        else:
            result=x%y
            save("%",x,y,result)
    elif opr == "/":
        if y == 0:
            print("Cannot divide by zero")
            continue
        else:
            result=x/y
            save("/",x,y,result)
    elif opr == "":
        print("Operator cannot be empty")
        continue
    else :
        print("invalid input")
        continue

    command=input("enter command or press enter").lower()

    if command=="history":
        if len(history) == 0:
            print("No history found")
        else:
            for item in history:
                print(item)

    elif command=="clear":
        result=None
        history.clear()

    elif command=="help":
        print("""
            history - show previous calculations
            clear   - clear history
            result  - show current result
            exit/no - quit calculator
        """)

    elif command=="exit" or command=="no":
        break

    elif command=="result":
        print (result)
    else:
        print("Invalid input")
        result = None
        continue
    