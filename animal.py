class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"
    
s = Student("Rahul", 90)
print(s)