print("print()")
print("---------------------------------------------------------")
text = "Print me!"
print(text)

print()

name = "John"
age = 25
print(f"{name} is {age} years old.")

print()
print("len()")
print("---------------------------------------------------------")
my_list = [1, 2, 3, 4, 5]
print("Length of my list:", len(my_list))

print()
print("range()")
print("---------------------------------------------------------")
for i in range(5):
    print(i)

print()
for j in range(10, 50, 10):
    print(j)

print()
print("type()")
print("---------------------------------------------------------")
num = 123
print(type(num))

text = "Hello, world!"
print(type(text))

print()
print("student_grades()")
print("---------------------------------------------------------")
def student_grades(students_dict):
    top_student = max(students_dict, key=students_dict.get)
    top_grade = students_dict[top_student]

    low_student = min(students_dict, key=students_dict.get)
    low_grade = students_dict[low_student]

    class_avg = sum(students_dict.values()) / len(students_dict)

    print(f"The student with the highest grade is {top_student} with a grade of {top_grade}.")
    print(f"The student with the lowest grade is {low_student} with a grade of {low_grade}.")
    print(f"The average grade of the class is {round(class_avg, 2)}.")

students_dict = {
    'John': 85,
    'Lisa': 79,
    'Tom': 86,
    'Anna': 90,
    'Mike': 75,
}

student_grades(students_dict)
