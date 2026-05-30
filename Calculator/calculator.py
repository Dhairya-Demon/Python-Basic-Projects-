from itertools import accumulate
import art
print(art.logo)



def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 -n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

output1 = add(44,76,)
output2 = sub(77,36)
output3= multiply(33,22)
output4 = divide(33,11)
#
# print(output1)
# print(output2)
# print(output3)
# print(output4)

calc = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,

}
def calculator():
    should_accumulate = True

    n1 = int(input("Type the first number "))

    while should_accumulate:
        for operation in calc:
            print(operation)
        operation_symbol = input("pick an operator ")
        n2 = int(input("Type the second number "))
        answer = calc[operation_symbol](n1,n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start new calculation")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n"*30)
            calculator()

calculator()