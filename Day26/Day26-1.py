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

