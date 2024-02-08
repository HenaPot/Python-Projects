import random


blueprint = [1, 1, -1]
my_list = [item + 1 for item in blueprint]
my_variable = all(item for item in blueprint)

# print(my_list)
# print(my_variable)

# print([number*2 for number in range(1, 5)])

names = ["Dzulzulejha", "Amir", "Senada", "Mujesira", "Mulekelefeleketa", "Zveznada"]
students = {student:random.randint(1, 100) for student in names}


# observe the fact that when iterating through eg. a list of tuples, you need to provide tuple as well
passed_students = {student : grade for (student, grade) in students.items() if grade >= 50}

some_ppl = passed_students.items()
for person in some_ppl:
    print(person)