import os
import openai
import sqlite3
import time

# Initialize the OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize SQLite database
conn = sqlite3.connect('chat_data.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS chats 
            (rowid INTEGER PRIMARY KEY,
            created_time INTEGER,
            message TEXT,
            role TEXT
          )''')

conn.commit()


def get_gpt_response(prompt):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion


# Main loop for the chat interface
while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        break

    # Capture the time right after user enters their message
    user_time = int(time.time())

    # Get the bot's response
    bot_response = get_gpt_response(user_input)

    # Capture the time right after getting API response
    assistant_time = int(time.time())

    # Save user message to database
    role = "user"
    c.execute("INSERT INTO chats (created_time, message, role) VALUES (?, ?, ?)",
              (user_time, user_input, role))
    conn.commit()

    # Extract bot's message and save it to database
    bot_reply = bot_response.choices[0].message['content']
    role = "assistant"

    c.execute("INSERT INTO chats (created_time, message, role) VALUES (?, ?, ?)",
              (assistant_time, bot_reply, role))
    conn.commit()

    print("Bot:", bot_reply)

# Close the SQLite database connection
conn.close()
