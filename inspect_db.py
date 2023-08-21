import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('chat_data.db')
c = conn.cursor()

# Fetch the first few (e.g., 5) rows from the table
c.execute("SELECT * FROM chats")

# Fetch all rows that the query returned
rows = c.fetchall()

# Print the rows
for row in rows:
    print(row)
    print("---")

# Close the SQLite database connection
conn.close()
