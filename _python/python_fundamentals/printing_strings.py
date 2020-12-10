print("this is a sample string")
name = "dwayne"
print("my name is " + name)
integer = 2
print(name, integer) # using comma is ok
# print(name + integer) # this throws an error, cannot concatenate string with number

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")
#F-string, allows insertion of variables into string, note the f at the beginning

print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# older way to insert variables into string - requires .format method

print("My name is %s and I'm %d" % (name, age))	
# even older way to insert variables into strings.  % is a placeholder - %s = string, %d = number




