### print() input()

john_name = "John"
john_age = 25
print(john_name)
print(john_age)
print(f"{john_name} is {john_age} years old.")

me = input("Who are you? ")
print(f"Hello, {me}!")

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

new_list = list(range(1,6))
print(new_list)

### type() str() int()

num = 123
text = "123"

print(type(num))
print(type(text))

print(type(str(num)))
print(type(int(text)))

### zip

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

dict = zip(names,ages)

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


### sort() sorted()

tuple = (3,5,2,1,4)

# tuple.sort()

new_list = sorted(tuple)

reverse_list = sorted(new_list, reverse=True)

reverse_list.sort()

reverse_list.reverse()

### filter()

def is_even(n):
    return n % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers2)
even_numbers = list(even_numbers)


### Dog daycare

def dog_ages(dogs_dict):
    oldest_dog = max(dogs_dict, key=dogs_dict.get)
    oldest_dog_age = dogs_dict[oldest_dog]

    youngest_dog = min(dogs_dict, key=dogs_dict.get)
    youngest_dog_age = dogs_dict[youngest_dog]

    average_age = sum(dogs_dict.values()) / len(dogs_dict)

    print(f"The oldest dog is {oldest_dog} with an age of {oldest_dog_age}.")
    print(f"The youngest dog is {youngest_dog} with an age of {youngest_dog_age}.")
    print(f"The average age of the dogs is {round(average_age, 2)}.")

dogs_dict = {
    'Rex': 7,
    'Buddy': 5,
    'Bella': 8,
    'Lucy': 6,
    'Max': 4,
}

dog_ages(dogs_dict)
