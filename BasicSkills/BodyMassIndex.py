''' Program: BMI Student Survey
Date written: 2 November 2020
Purpose: 5 students name, height, weight
get calculate BMI '''

class Student:
    def __init__(self, name, weight, height):
       self.name = name
       self.weight = weight
       self.height = height
    
    @staticmethod
    def user_input():
        while True:
            try:
                name = input("Enter Name: ")
                if not name.isalpha():
                    print("only letters are allowed!")
                    raise ValueError
                weight = float(input("Enter weight(kg): "))
                height = float(input("Enter height(m): "))
                BMI = weight/(height*height)
                return BMI, name
            except:
                print('InvaildInput')
                continue

students = []
while len(students) < 2:
    print(f"\n\n-------- Student {len(students)+1} --------")
    student = Student.user_input()
    students.append(student)

for i in range(len(students)):
    if [x[0] for x in students][i] < 18.5:
        print(f"{[x[1] for x in students][i]} is underweight")
        print(students)
    elif [x[0] for x in students][i] > 18.5 and [x[0] for x in students][i] < 27:
        print(f"{[x[1] for x in students][i]} is a healthy weight")
        print(students)
    elif [x[0] for x in students][i] > 27:
        print(f"{[x[1] for x in students[i]]} is overweight")
        print(students)
