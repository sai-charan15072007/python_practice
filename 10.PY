# def find (values):
#     minimum = min(values)
#     maximum = max(values)
#     avg= sum(values)/len(values)
#     return minimum,maximum,avg
# num=[15,30,45,25,90,100]
# minimum,maximum,avg = find(num)
# print("minimum:",minimum)
# print("maximum=",maximum)
# print("average=",avg)


def grade(marks):
    total= sum(marks)
    percentage=total/len(marks)
    if percentage>=90:
        grade="A+"
    elif percentage>=80:
         grade ="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C" 
    elif percentage>=50:
        grade="D"
    else:
        grade="fail"
    return total,percentage,grade
marks = []
for i in range(5):
    mark=int(input(f"enter marks of subject{i+1}:"))
    marks.append(mark)
total,percentage,grade = grade(marks)
print("\n-----Result-----")
print("Total Marks:",total)
print("percentage:",percentage)
print("grade:",grade)