# SQLite Chat Conversation Saver

This script allows you to have a conversation with a GPT-3.5 Turbo assistant and saves both your messages and the assistant's replies into a SQLite database. It uses the OpenAI API for interaction and Python's built-in SQLite library for database operations.

## Features

- Interactive chat interface
- Real-time response fetching from OpenAI API
- Saves chat data into a SQLite database
- Uses local Unix timestamps for each message

## Prerequisites

- Python 3.x
- OpenAI Python package
- SQLite

## Database Schema

The SQLite database has a table named `chats` with the following columns:

- `rowid`: Unique row identifier (Primary Key)
- `created_time`: Unix timestamp for when the message was created
- `message`: The message text
- `role`: The role of the message sender ("user" or "assistant")

## Have a look...

- use the inspect_db.py to have a quick look at the saved rows

