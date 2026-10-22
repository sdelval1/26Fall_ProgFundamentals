import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS books")

cur.execute ("""CREATE TABLE books
(   id INT NOT NULL,
    TITLE VARCHAR(50) NOT NULL,
    AUTHOR VARCHAR(50) NOT NULL,
    YEAR INT,
    GENRE VARCHAR(20),
    COPIES INT,
    RATING INT,
    PRIMARY KEY (id));
""")


cur.execute("""
INSERT INTO books
VALUES (1, "You've Reached Sam", "Dustin Thao", 2021, "Fiction", 2, 3);
""")

books = [
    (2, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fiction", 5, 4),
    (3, "Frankenstein", "Mary Shelley", 1818, "Fiction", 1, None),
    (4, "The Streets of Panic Park", "R.L. Stine", 2009, "Fiction", 5, 5),
    (5, "The Murder of Roger Ackroyd", "Agatha Christie", 1926, "Fiction", 1, None),
    (6, "A Brief History of Time: From the Big Bang to Black Holes", "Stephen Hawking", 1988, "Non-Fiction", 1, 1),
]

cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", books)

print("Books published after 1990:")
for row in cur.execute("SELECT TITLE, AUTHOR FROM books WHERE YEAR > 1990"):
    print(row[0])

print("Fiction books with more than two copies: ")
for row in cur.execute("SELECT TITLE FROM books WHERE GENRE = 'Fiction' AND COPIES > 2"):
    print(row[0])

print("Books printed before 1900s or rated 5: ")
for row in cur.execute("SELECT TITLE FROM books WHERE YEAR < 1900 OR RATING = 5"):
    print(row[0])

print("Books not in the mystery genre: ")
for row in cur.execute("SELECT TITLE FROM books WHERE NOT GENRE = 'mystery'"):
    print(row[0])

print("Books that are in the Science or History genre: ")
for row in cur.execute("SELECT TITLE FROM books WHERE GENRE IN ('History', 'Science')"):
    print(row[0])

letters = input("Choose a letter: ")
print("Books with Authors who's names start with the letter: " + letters)
for row in cur.execute("SELECT TITLE FROM books WHERE AUTHOR LIKE ?", (letters + "%",)):
    print(row[0])

print("Books with no rating: ")
for row in cur.execute("SELECT TITLE FROM books WHERE RATING IS NULL"):
    print(row[0])


conn.commit()
conn.close()
