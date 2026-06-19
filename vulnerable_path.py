# vulnerable_path.py

def read_file(filename):
    with open("uploads/" + filename, "r") as f:
        return f.read()

user_input = input("File: ")
print(read_file(user_input))
