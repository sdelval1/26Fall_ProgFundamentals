import sqlite3

conn = sqlite3.connect("StudentRecords.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute ("""CREATE TABLE StudentRecords
(   id INT NOT NULL,
    Name VARCHAR(20) NOT NULL,
    Age INT NOT NULL,
    Major VARCHAR(50) NOT NULL,
    PRIMARY KEY (id));
""")

StudentRecords = [
    (1, "Sammy", 23, "Computer Science"),
    (2, "Jose", 20, "Computer Science"),
    (3, "Rando", 19, "Health Sciences"),
    (4, "Jesse", 25, "Nursing"),
    (5, "MJ", 18, "Dance"),

]

cur.executemany("INSERT INTO StudentRecords VALUES (?, ?, ?, ? )", StudentRecords)

print("Student Names, Age, and Major's: ")
for row in cur.execute("SELECT Name, Age, Major FROM StudentRecords"):
    print(row)

#need to ask user for a new student and if yes move on, if not repeat
new_name = ""
new_student_age = ""
new_student_major = ""


user_input = "no"

while user_input == "no":
    user_input = input("Would you like to add a student? ")
    if user_input == "yes":
        print("")
    else:
        pass




while new_name == "":
    new_name = input("What is the name of the new student? ")
    if new_name == "":
        print("Please enter a valid name")
    else:
        print("Thank you " + new_name)

while new_student_age == "":
    new_student_age = input("What is the age of the new student? ")
    if new_student_age == "":
        print("invalid age")
    elif new_student_age <= "17":
        print("invalid age")
    else:
        pass

while new_student_major == "":
    new_student_major = input("What is the new students major? ")
    if new_student_major == "":
        print("Invalid major")
    else:
        pass

new_info = [
    (6, new_name, new_student_age, new_student_major)
]

cur.executemany("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", new_info)

conn.commit()
conn.close()
