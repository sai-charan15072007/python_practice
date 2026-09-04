class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"{self.name} scored {self.marks}"
    def __repr__(self):
        return f"student({self.name},{self.marks})"
s=student("rahul",90)
print(s) 