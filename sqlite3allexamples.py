import sqlite3

# #  ------- EXAMPLE 1 -------
# # Basic introduction to sqlite3
#
# # In RAM
# # conn = sqlite3.connect(':memory:')
#
# # As a file
# conn = sqlite3.connect('example.db')
#
# print("Opened database succeessfully!")
#
# # Grab the cursor object from the database
# cursor = conn.cursor()
#
# # The cursor allows you to excute the commands
# # The conn object doesn't allow you to excute commands only to connect to the database
#
# # cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
# cursor.execute('''INSERT INTO users VALUES(1, "Kiriphorito", "hello World")''')
# # cursor.execute("INSERT INTO users VALUES(1, 'Kiriphorito', 'hello World')")
#
# # Saves the changes to the file
# conn.commit()
#
# # Closes the connection to the file to ensure proper closure.
# conn.close()

#  ------- EXAMPLE 2 -------
# Putting it into a function

# def addUser():
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users VALUES(2, 'Blah', 'bkah')")
#     conn.commit()
#     conn.close()
#
# addUser()

# #  ------- EXAMPLE 3 -------
# # Using parameters and variables
#
# def addUser(id, username, password):
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     query = "INSERT INTO users VALUES(" + str(id) + ",'" + username + "','" + password + "')"
#     cursor.execute(query)
#     conn.commit()
#     conn.close()
#
# addUser(2, 'Taylor', 'bkah')

#  ------- EXAMPLE 4 -------
# Using placeholders

# def addUser():
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users VALUES(?,?,?)", (4, "Senro", "Tay"))
#     conn.commit()
#     conn.close()
#
# addUser()

# #  ------- EXAMPLE 5 -------
# # Using placeholders and parameters
#
# def addUser(id, username, password):
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users VALUES(?,?,?)", (id, username, password))
#     conn.commit()
#     conn.close()
#
# addUser(5, "Kevin", "Tay")

# #  ------- EXAMPLE 6 -------
# # Adding muliple records using for each
#
# def addUser(data):
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     for record in data:
#         cursor.execute("INSERT INTO users VALUES(?,?,?)", record)
#     conn.commit()
#     conn.close()
#
# data = [
#     (6, "S", "P"),
#     (7, "A", "H"),
#     (8, "M", "A"),
# ]
#
# addUser(data)

# #  ------- EXAMPLE 7 -------
# # Adding muliple records using for each
#
# def addUser(data):
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     cursor.executemany("INSERT INTO users VALUES(?,?,?)", data)
#     conn.commit()
#     conn.close()
#
# data = [
#     (9, "R", "K"),
#     (10, "A", "H"),
#     (11, "E", "A"),
# ]
#
# addUser(data)

# #  ------- EXAMPLE 8 -------
# # Using with
#
# # "with" gurantees that the database will commit and close after the with block has finished
#
# def addUser(id, username, password):
#     with sqlite3.connect('example.db') as conn:
#         cursor = conn.cursor()
#         query = "INSERT INTO users VALUES(" + str(id) + ",'" + username + "','" + password + "')"
#         cursor.execute(query)
#
# addUser(12, 'Mike', 'Day')

# #  ------- EXAMPLE 9 -------
# # Using with
#
# # You can also use with like below
#
# def addUser(id, username, password):
#     conn = sqlite3.connect('example.db')
#     with conn:
#         cursor = conn.cursor()
#         query = "INSERT INTO users VALUES(" + str(id) + ",'" + username + "','" + password + "')"
#         cursor.execute(query)
#
# addUser(13, 'Steve', 'Jobs')


#  ------- EXAMPLE 9 -------
# What is the try - except block

# Part 1 - What do you notice?
# x = 3 / 0
# print("But you will notice code will still run")


# Part 2 - What do you notice?
# try:
#     x = 3 / 0
# except:
#     print("You trid to divide with zero")
# print("But you will notice code will still run")

# With this you can use this in the database so that it doesn't crash the entire program if
# something were to go wrong
#
# #  ------- EXAMPLE 10 -------
#
# # You can use this for your application so that it doesn't crash if something where to go wrong
#
# def addUser():
#     id = 1
#     username = "sdfsdf"
#     password = "sdfsdf"
#     with sqlite3.connect('example.db') as conn:
#         cursor = conn.cursor()
#         query = "INSERT INTO users VALUES(" + str(id) + ",'" + username + "','" + password + "')"
#         try:
#             cursor.execute(query)
#         except:
#             print("Not a unique ID")
#         print("This code will still run!")
#
# addUser()

#  ------- EXAMPLE 11 -------

# Show result

def showAllUsers():
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users"
        try:
            result = cursor.execute(query)
            for row in result:
                print(row)
        except:
            print("Query error?")

showAllUsers()


