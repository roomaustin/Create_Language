import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("ai_learning.db")
cursor = conn.cursor()

# Create a table for programming languages
cursor.execute("""
    CREATE TABLE IF NOT EXISTS programming_languages (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
""")

# Sample data to be inserted into the database
programming_languages_data = [
    ("Python", "A high-level programming language known for its simplicity and readability."),
    ("Java", "A widely-used, platform-independent programming language."),
    ("JavaScript", "A popular scripting language often used for web development."),
    # Add more programming languages and descriptions as needed
]

# Insert sample data into the table
for language in programming_languages_data:
    cursor.execute("INSERT INTO programming_languages (name, description) VALUES (?, ?)", language)

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("Database and table created, and data inserted successfully.")
