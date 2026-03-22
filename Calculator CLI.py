import time

def strtolist(string):
    number = ""
    tokens = []   # renamed from list

    for i in string:
        if i.isdigit() or i == ".":
            number += i
        else:
            if number != "":
                tokens.append(float(number))
                number = ""
            tokens.append(i)

    if number != "":
        tokens.append(float(number))

    return tokens


def calculate(EQ):
    # Operator priority
    for op in ["*", "/", "+", "-","^"]:
        while op in EQ:
            index = EQ.index(op)

            if op == "^":
                result = EQ[index-1] ** EQ[index+1]
            elif op == "*":
                result = EQ[index-1] * EQ[index+1]
            elif op == "/":
                result = EQ[index-1] / EQ[index+1]
            elif op == "+":
                result = EQ[index-1] + EQ[index+1]
            elif op == "-":
                result = EQ[index-1] - EQ[index+1]

            EQ[index-1] = result
            del EQ[index:index+2]

    return EQ[0]
print("Welcome to AKM Calculator CLI")
print({"Add":"+","Subtract":"-","Multiply":"*","Division":"/","Power":"^"})
while True:
    print()
    Equation = input("Enter your equation: ")
    print()
    try:
        EQ = strtolist(Equation)
        print("this is your equation:", EQ)
        print()
        print("Calculating...")
        time.sleep(3)
        print("We are Just near to solution")
        time.sleep(2)

        print("Result:", calculate(EQ))
    except Exception as e:
        print("Invalid input:", e)
    time.sleep(1)