
# 'else' will run only if 'try' succeed
# 'finally' will run no matter what
# 'raise' create your own errors

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("New text line")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
# finally:
#     file.close()
#     print("file was closed")
finally:
    raise TypeError("This is an error that I made up")
