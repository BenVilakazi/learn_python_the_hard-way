def add(a, b):
    print(">>>")
    print(f"ADDING {a} + {b}")
    print("<<< exit")
    return a + b

def sub(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def mul(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def div(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = sub(78, 4)
print(">>> height=", height)
weight = mul(90, 2)
iq = div(100, 2)

print(f"Age: {age}, Height: {height}, weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, sub(height, mul(weight, div(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")