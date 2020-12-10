import random
def randInt(min = 0, max = 100):
    if type(min) != int or type(max) != int or max < min:
        num = "invalid input"
    elif max == min:
        num = min
    else:
        num = round(random.random() * max + min)
    return num
print(randInt()) 		            # should print a random integer between 0 to 100
print(randInt(max=50)) 	            # should print a random integer between 0 to 50
print(randInt(min=50)) 	            # should print a random integer between 50 to 100
print(randInt(min=50, max=500))     # should print a random integer between 50 and 500

# edge cases
print(randInt(min=500, max=250))
print(randInt(min=5, max=5))
print(randInt(min=5.3, max=5.4))
print(randInt(min="hello", max=5))
