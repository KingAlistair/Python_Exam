### input and output

### print()

name = "John"
age = 25
print(name)
print(age)
print(f"{name} is {age} years old.")

name = input("Who are you? ")
print(f"Hello, {name}!")



### sum()

numbers = [1,2,3,4,5]

custom_sum = 0
for number in numbers:
        custom_sum += number

print(custom_sum)

print(sum(numbers))


### len()

my_list = [1, 2, 3, 4, 5]
my_string = "What is my length?"
print("Length of my list:", len(my_list))
print(my_string, len(my_string))


### range()

for j in range(0, 11, 2):
    print(j)

### list() range()

new_list = list(range(1,6))
print(new_list)


### type() str() int()

number = 123
text = "123"

print(type(number))

print(type(text))

print(type(str(number)))

print(type(int(text)))

### zip

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

dict = dict(zip(names,ages))

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

### sort() sorted()

tuple = (3,1,5,2,4)

tuple.sort() # Error

sorted_list = sorted(tuple) 
print(sorted_list) 

reverse_list = sorted(sorted_list, reverse=True)
print(reverse_list) 

sorted_list.reverse()
print(sorted_list)

sorted_list.sort()
print(sorted_list)


### student_grades

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
