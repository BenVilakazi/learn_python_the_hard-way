# this one is like script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# the above *args isointless,do the below instead

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_one(arg1):
    print(f"arg1: {arg1}")
    
def print_none():    
    print("I got nothing")
    
print_none()
print_one("First!")
print_two("Ben", "Viliakazi")
print_two_again("Ben", "Vilakazi")