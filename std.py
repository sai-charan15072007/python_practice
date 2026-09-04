class student:
    static section,course=F,CSE
    def __init__(self,name,age,roll,marks):
        self.name=name
        self.age=age
        self.roll=roll
        self.marks=marks
    def display(self):
        print("STUDENT DETAILS")
        print("Name:",self.name)
        print("Roll number:",self.roll)
        print("Age:",self.age)     
        print("Section:",section)
        print("Course:",course)
        print("Marks:",marks)
s1=student("venkat",20,"BH",90)
s1.display()        


       