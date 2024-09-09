thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

'''
tuple lo items add inka remove cheyyalem so 1st we have to change tuple to list add the element and change the list again to tuple
'''


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#we can add tuple to a tuple