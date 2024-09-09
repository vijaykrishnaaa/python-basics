#using list method
yoho = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(yoho)
print(yoho[2:5])
print(yoho[:4])
print(yoho[2:])
print(yoho[-4:-1])
if "apple" in yoho:
  print("Yes, 'apple' is in the fruits list")