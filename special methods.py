class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def __str__(self):
        return f"name={self.name},roll={self.roll},marks={self.marks}"
    def __repr__(self):
        return f"student({self.name},{self.roll},{self.marks})"
    def __eq__(self,other):
        if isinstance(other,student):
            return self.roll==other.roll
        return False
s1=student("rahul",1,90)
S2=student("rohit",1,80)
S3=student("rohit",2,80)
print(s1)
print(repr(s1))
print(s1==S2)