class student:
    def __init__(self,marks,name):
        self.marks = marks
        self.name = name
    def __str__(self):
        return f"name={self.name}\nMarks={self.marks}"
s=student(90,"John")
print(s)