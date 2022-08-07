# file not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdegr"])
except ModuleNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError:
    print("that key dose not exist")
# or:
except KeyError as error_message:
    print(f"the key {error_message} does not exist.")
# if the errors are fixe else will be work and the file will be read.
else:
    content = file.read()
    print(content)
# when we want the code execute use finally:
finally:
    file.close()
    print("file was closed.")


