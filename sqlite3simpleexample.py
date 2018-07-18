import sqlite3

# In RAM
# conn = sqlite3.connect(':memory:')

# As a file
conn = sqlite3.connect('test.db')

print("Opened database succeessfully!")

# Grab the cursor object from the database
cursor = conn.cursor()

# The cursor allows you to excute the commands
# The conn object doesn't allow you to excute commands only to connect to the database

# Executing SQL commands/queries
# cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER )''')
cursor.execute('''INSERT INTO users VALUES(5, "Rae", 16)''')

# Saves the changes to the file
conn.commit()

# Close the connection
conn.close()
