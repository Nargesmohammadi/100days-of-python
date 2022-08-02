# file = open("my_file.txt")
# open and read the file.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# open and write the file, use append in mod=
with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")


