import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#THIS IS BAD CODE
#Runs at O(N^2) since each list item must be compared across N names from second list.
#Since N items need to be checked N times, it is O(N^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


#initialize Binary Search Tree with first value of first list.
bst = BinarySearchTree(names_1[0])

#go through entire names list from first document
for name in names_1:
    #and add it to the Binary Search Tree
    bst.insert(name)
#for the second list of names
for name in names_2:
    #if a given name is contained in the BST (AKA - a duplicate entry!)
    if bst.contains(name):
        #append it to the duplicates list.
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
