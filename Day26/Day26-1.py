# name = "Mitra"
# letters_list = [letter for letter in name]
# print(letters_list)

x = range(1, 5)
new_x = [num * 2 for num in x]
print(new_x)

# names = ["Arash", "Ali", "Mehdi", "Donya"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

names2 = ['Alex', 'Caroline', 'David', 'Ali']
long_name = [name.upper() for name in names2 if len(name) > 5]
print(long_name)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_number = [num * num for num in numbers]
print(new_number)

new_number1 = [num for num in numbers if num % 2 == 0]
print(new_number1)

with open("file1.txt") as file1:
    file_1_data = file1.read()

with open("file2.txt") as file2:
    file_2_data = file2.read()

result = [int(num) for num in file_1_data if num in file_2_data]


