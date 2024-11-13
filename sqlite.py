import sqlite3
import os
# import termcolor

DATABASE_NAME="student.db"
## If the database already exist then remove otherwise it will produce error
if os.path.isfile(DATABASE_NAME):
    os.remove(DATABASE_NAME)

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
table_info="""
    Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR (25), SECTION VARCHAR(25))
    """
cursor.execute(table_info)
cursor.execute('''Insert into STUDENT values ('Krish','Data Science','A')''')
cursor.execute('''Insert into STUDENT values ('Ravi','ML Engineer','B')''')
cursor.execute('''Insert into STUDENT values ('Vivek','MLOps','A')''')
cursor.execute('''Insert into STUDENT values ('Vishesh','Data Science','A')''')

print("The inserted records are: ")
data = cursor.execute("select * from STUDENT")
for row in data:
    print(row)

connection.commit()
connection.close()