i = 0
num = []

while i < 6:
    print(num)
    print(f"At the top i is {i}")
    num.append(i)
    
    i = i + 1
    print("Numbers now: ", num)
    print(f"At the bottom i is {i}")
    
    
print("The numbers: ")

for n in num:
    print(n)