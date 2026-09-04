class student:
    def __init__(self, name, roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("student details")
        print("name:", self.name)
        print("roll:", self.roll)
        print("marks:",self.marks)
s1 = student("sravani",1,98)
s1.display()