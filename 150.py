#positional only argument

def my_function(x, /):
  print(x)

my_function(3)

'''
def my_function(x, /):
  print(x)

my_function(x = 3)    this is wrong
'''

#Keyword-Only Arguments

def my_function(*,x):
  print(x)
my_function(x=3)

'''
def my_function(*, x):
  print(x)

my_function(3) this is wrong 

'''

#combined both positional and keyword

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)