people = 20
cats = 30 
dogs = 15 

if people < cats:
    print(">>> people < cats")
    print("Too many cats! The world is doomed!")
    print("<<< exit")

if people > cats:
    print(">>> people > cats")
    print("Not many cats! The world is saved!")
    print("<<< exit")

if people < dogs:
    print(">>> people < dogs")
    print("The world is drooled on!")
    print("<<< exit")
    
if people > dogs:
    print(">>> people > dogs")
    print("The world is dry!")
    print("<<< exit")
    
dogs += 5

if people >= dogs:
    print(">>> people >= dogs")
    print("People are greater than or equal to dogs.")
    print("<<< exit")
    
if people <= dogs:
    print(">>> people <= dogs")
    print("People are less than or equal to dogs")
    print("<<< exit")
    
if people == dogs:
    print(">>> people == dogs")
    print("People are dogs.")
    print("<<< exit")