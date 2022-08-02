# open and read the file.
# absolute
with open("/home/mitraa/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# relative
with open("../../Desktop/my_file.txt") as f:
    contents = f.read()
    print(contents)



