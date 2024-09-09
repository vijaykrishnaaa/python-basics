#slicing strings 
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b.upper()) #upper case
print(b.lower()) #lower case
print(b.strip()) # returns "Hello, World!" , The strip() method removes any whitespace from the beginning or the end:
print(b.replace("H", "J"))
print(b.split(",")) # returns ['Hello', ' World!']
