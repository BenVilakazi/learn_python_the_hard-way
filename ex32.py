count = [1, 2, 3, 4, 5]
fruits = ['apples', 'bananas', 'oranges', 'pears']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in count:
    print(f"This is count {number}")
    
# same as above

for fruit in fruits:
    print(f"A type of fruit {fruit}")
    
# also we can go through mixed list too 
# notice we have to use {} since we don't know what's in it

for i in change:
    print(f"i got {i}")
    
# we can also build lists, first start with an empty one

elem = []

# then use the range function to do 0 to 5 counts

for i in range(0,6):
    print(elem)
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elem.append(i)
    
#now we can print them out too
for i in elem:
    print(f"element was: {i}")
    print(elem)