import math
def add(x,y): return x + y
def sub(x,y): return x - y
def mul(x,y): return x * y
def div(x,y): return x / y

while True:
    try:
        op = input("Enter +, -, *, / or 'exit' ")
        if op == 'exit':
            print("Goodbye!")
            break

        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if op == '+': res = add(num1,num2)
        elif op == '-': res = sub(num1,num2)
        elif op == '*': res = mul(num1,num2)
        elif op == '/': res = div(num1,num2)
        else:
            print("Invalid Operator!")
            
        print("Exact value: ", res)
        print("Rounded value: ",res)
        #continue

    except ValueError:
        print("You have to write a number !")
    except ZeroDivisionError:
        print("Invlaid, it cannot be divided by 0,zero,. ")
