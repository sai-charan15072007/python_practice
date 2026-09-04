class student:
    def __init__(self,name):
        self.name=name
    def __eq__(self,age):
        return self.name==age.name
s1=student("13")
s2=student("rahul")
s3=student("13")
print(s1==s2)
print(s2==s3)