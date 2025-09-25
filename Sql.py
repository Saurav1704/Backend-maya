import sqlite3
def save_feedback_to_db(question, response, rating):
    try:
        connection = sqlite3.connect("feedback.db")
        cursor = connection.cursor()

        # Ensure table exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chatbot_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                response TEXT,
                rating INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Insert feedback record
        cursor.execute('''
            INSERT INTO chatbot_feedback (question, response, rating)
            VALUES (?, ?, ?)
        ''', (question, response, rating))

        connection.commit()
        connection.close()
        print("Feedback saved")
        return True
    except Exception as e:
        print("Error inserting feedback:", e)
        return False
