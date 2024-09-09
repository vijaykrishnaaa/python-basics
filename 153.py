class student:
    def __init__(self,name,age):
        self.name=name   #ikada manam self badulu emaina pettochu 
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"
s1=student("vijay",19)
s2=student("elf",20)
s3=student("reddy",24)

print(s1.age)
print(s3.name)