#list comprehensions

my_list = [x*2 for x in range(1,11)]
print(my_list)

my_list1 = [x for x in range(1,100) if x % 10 == 0]
print(my_list1)


#Skill Group 1
#Use a for loop to modify elements of a list.

#Use the list.append() method.

#Use the string.endswith() and string.replace() methods to modify the elements within a list.

list = ["Jan 2023", "Feb 2025", "Mar 2023", "Apr 2023", "Aug 2025"]
updated_list = []

for elements in list:
    if list.endswith("2023"):
        new_list = list.replace("2023", "2024")
        updated_list.append(new_list)
    else:
        updated_list.append(list)
print(updated_list)

#Skill Group 4
#Use the string.split() method to separate a string into a list of individual words.

#Iterate over the new list using a for loop.

#Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the substring to the end of the element.

#Convert a list back into a string.

def change_string(old_string):
    new_string = ""

    new_list = change_string.split()

    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string

print(change_string("1one 2two 3three 4four 5five"))