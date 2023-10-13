chickens = 30
goat = 40
sheep = 15

if goat > chickens:
    print("We should take the goat")
elif goat < chickens:
    print("We shouldn't take the goats")
else:
    print("We can't decide")
    
if sheep > goat:
    print("That's too many sheep")
elif sheep < goat:
    print("Maybe we should take the sheep")
else:
    print("We still can't decide")
    
if chickens > sheep:
    print("Alright, let's just take the sheep.")
else:
    print("Fine, let's stay home then.")