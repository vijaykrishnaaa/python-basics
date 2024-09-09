thisdict = {
  "brand": "Ford", #ikada brand anedi key inka ford anedi value
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#there is also a method called key()

x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)


''''''
#replacing year value

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

''''''

''''''
#adding a new key value pair

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

''''''

x = thisdict.items()
print(x) #Get a list of the key:value pairs


''''''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


''''''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #The pop() method removes the item with the specified key name:
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()#The popitem() method removes the last inserted item
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]#The del keyword removes the item with the specified key name:
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict#this will delete whole dictionary
print(thisdict) #this will cause an error because "thisdict" no longer exists.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()#The clear() method empties the dictionary:
print(thisdict)

''''''

