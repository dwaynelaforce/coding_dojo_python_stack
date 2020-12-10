# 1. Print 1-255
# Print all the integers from 1 to 255. 

# for i in range(1, 256):
#     print(i)
#works!


# 2. Print Odds 1-255
# Print all odd integers from 1 to 255. 

# for i in range(1, 256):
#     if i % 2 != 0:
#         print(i)
#works!

# 3. Print Ints and Sum 0-255
# Print integers from 0 to 255, and with each integer print the sum so far. 

# sum = 0
# for i in range(256):
#     print(i)
#     sum += i
#     print(sum)
#works!

# 4. Iterate and Print Array
# Iterate through a given array, printing each value. 

# def Iterate(listy):
#     for i in listy:
#         print(i)
# listy_list = [5,6,8,9,4,5,2,3,6]
# Iterate(listy_list)
#works!

# 5. Find and Print Max
# Given an array, find and print its largest element. 

# def find_max(listy):
#     max = listy[0]
#     for i in listy:
#         if i > max:
#             max = i
#     print(max)
# list5 = [-9,5,6,8,7,1,0]
# find_max(list5)
#works!

# 6. Get and Print Average
# Analyze an array’s values and print the average. 


# def average(listy):
#     sum = 0
#     for i in listy:
#         sum+=i
#     avg = sum / len(listy)
#     print(avg)
# list6 = [1,2,3,4,5,6,8,9]
# average(list6)
#works!

#                     (O_>O) &*""   '   (*o*)


# 7. Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).  

# listy = []
# for i in range(1, 256):
#     if i % 2 != 0:
#         listy.append(i)
# print(listy)
#works!


# 8. Square the Values
# Square each value in a given array, returning that same array with changed values. 

# def squareTheValues(listy):
#     for i in range(len(listy)):
#         listy[i] *= listy[i]
#     return listy
# print(squareTheValues([1,2,3,4,5,1000]))
#works!

#                     (O_>O) &*""   '   (*o*)

# 9. Greater than Y
# Given an array and a value Y, count and print the number of array values greater than Y. 

# def greaterThanY(listy, y):
#     count = 0
#     for i in listy:
#         if i > y:
#             count+=1
#     print(count)
# greaterThanY([5,8,9], 5)


# 10. Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero. 

# def zeroOutNegative(listy):
#     for i in range(len(listy)):
#         if(listy[i] < 0):
#             listy[i] = 0
#     return listy# print(zeroOutNegative([1,2,-3,4,-5]))

# 11. Max, Min, Average
# Given an array, print the max, min and average values for that array.

# def maxMinAverage(listy):   ***********
#     sum=0
#     min=listy[0]
#     max=listy[0]
#     for i in listy:
#         sum+=i
#         if min>i:
#             min = i
#         elif max<i:
#             max = i
#     avg = sum/len(listy)
#     print("max is ", max, "min is ", min, "avg is", avg)
# listy_list = [1,3,6,-5,8]
# maxMinAverage(listy_list)
#works!



# 12. Shift Array Values
# Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.

#didn't finish

# def shiftValues(listy):
#     for i in range(1, len(listy), 1):
#         listy[i-1] = listy[i]
#     len(listy) =
#     return listy
# print(shiftValues([1,2,3,4,5,6,7,8,9]))


# 13. Swap String For Array Negative Values
# Given an array of numbers, replace any negative values with the string 'Dojo'.

# def swapStringValues(listy):

