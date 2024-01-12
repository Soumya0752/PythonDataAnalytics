import mysql.connector

# Replace these values with your MySQL server details
host = 'localhost'
user = 'root'
password = 'Soumya@1234'
database = 'mobileapp4'

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a SELECT query
query = "SELECT * FROM mobile"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Iterate through the rows and print the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
