import random
listy_list = []
items_in_list = 1000
for x in range(items_in_list):
    listy_list.append(round(random.random()*100000))
print("unsorted list is ", listy_list)
for x in range(len(listy_list)-1):
    for i in range(len(listy_list)-1):    
        if listy_list[i] > listy_list[i+1]:
            listy_list[i], listy_list[i+1] = listy_list[i+1], listy_list[i]
print(listy_list)