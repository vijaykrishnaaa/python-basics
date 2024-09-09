"""
x="awesome"
def rey():
    x="reddy"
    print("hello "+x)
rey()
print(x)
"""



def rey():
    global x
    x="reddy"
    print("hello "+x)
rey()
print(x)