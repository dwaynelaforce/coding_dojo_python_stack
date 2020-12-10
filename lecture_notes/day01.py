# primitive data types
some_string = "some value" # string
some_number = 123 # integer
some_decimal = 1.23 # float (decimal)
some_boolean = True # boolean (has to be capitalized)
some_boolean2 = False
some_none = None # none == null

# composite data types (structures)
some_list = [1,2,3] # list (equivalent of array in JS)
some_list.append(4) # .append (equivalent of .push in JS)
some_list.pop() # .pop (same as JS)

some_dictionary = { # dictionary (equivalent of object in JS) 
    "some_key": "some value", # separate elements with comma
    "some_other": 123
}
some_dictionary["some_key"] # returns the value of that key in the dict

# built-in functions
print("string") # print - equivalent of console.log in JS
print(123) # number
print(some_list) # variable

len(some_list) # len (length) (equivalent of .length in JS)
len("string") # will print the number of characters in string
len(some_dictionary) # will print the number of key-value pairs in the dict

type(some_string) # type (similar to typeof in JS) returns the type of object e.g. string, number, boolean etc.

# range() # range - takes up to 3 arguments, minimum of 1, essentialing produces a list of all numbers to loop through
# range(stop) # just the stopping point (exclusive), start point is assumed to be 0, increment is assumed to be 1
# range(start, stop) # increment is assumed to be 1
# range(start, stop, increment)
range(1, 10, 1) #evaluates to [1,2,3,4,5,6,7,8,9]


# code block / code body
if 5 > 2: # this is the code block (no parenthesis or curly brackets)
    print("5 is more than 2") # this is the code body - must be indented to be considered part of the code block

# conditionals
num1 = 1
num2 = 2
if num1 < num2:
    print("num1 greater than num2")
elif num1 > num2:                           # elif - equivalent of else if, have as many as you want
    print("num1 less than num2")
else:
    print("num1 and num2 are equal")

# loops
#for <variable> in <object>   - object can be range, list, variable etc. variable is the iterator
for i in range(0, 10, 1):
    print(i)

listy_list = [2,4,6,8]
for i in listy_list:              # use to reference the values
    print(i)                      # will print each value in the list (not the index), 

for i in range(len(listy_list)):  # use to do something with the values
    print(listy_list[i])          # will do the same
    listy_list[i] = 0             # will change the value of each index to 0

# while <conditional>  - generally avoid but can use
start = 0
while start < 10:
    print(start)
    start += 1

# functions
# def function_name(parameters):    - "def" tells the PC you are defining a function, must define function ahead of its call
def func_name(parameter):
    print(parameter)              # code boy of the function
func_name(123)                    # this calls the function
