import os

print(os.path.exists("notes.txt"))

try:
    os.remove("notes.txt")
    print("notes.txt was deleted")
except FileNotFoundError:
    print("There is no notes.txt to delete")
with open("notes.txt", "w") as f:
    f.write("buy dog food\n")
    f.write("Walk the dog.\n")

with open ("notes.txt", "a") as f:
    f.write("Brush the dog\n")

with open ("notes.txt", "r") as f:
    contents = f.read()
print(contents)

with open("notes.txt", "r") as f:
    for line in f:
        print("To do: ", line.strip())
