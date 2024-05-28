"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Work some of the more advanced features of lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Here is a list of 10 fruits:
fruits = ["Grape", "Apple", "Lemon", "Cherry", "Date", "Elderberry", "Fig",  "Honeydew", "Kiwi", "Banana"]


# Remove the third fruit from the list using the pop() method.
third_fruit = fruits.pop(2)
print(fruits)

# Use the remove() method to remove a fruit of your choice from the list.

fruits.remove("Cherry")
print(fruits)


# Search for "Apple" in the list and print a message saying whether or not it was found.

if "Apple" in fruits:
    print("apple found in fruits!")
else:
    print("apple is not found :C")

# Sort the List in alphabetical order.

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon",]


# Create a new list that contains a slice of the first 5 items
sliced_fruits = ["Slice of Apple", "Slice of Banana", "Slice of Cherry", "Slice of Date", "Slice of Elderberry"]

# Print out the new sliced list using a for loop

print(sliced_fruits)