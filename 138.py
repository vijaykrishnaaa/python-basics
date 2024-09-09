# adding element
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#adding two sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)




thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset.update(mylist)
print(thisset)