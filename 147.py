fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

print("---------------------------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("---------------------------------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("---------------------------------------")

for x in range(6):
  print(x)

print("---------------------------------------")
for x in range(2, 6):
  print(x)

print("---------------------------------------")

for x in range(2, 30, 3):
  print(x)

print("---------------------------------------")

adj=["red","blue","big"]
name=["apple","sky","tree"]

for x in adj:
    for y in name:
        print(x, y)

