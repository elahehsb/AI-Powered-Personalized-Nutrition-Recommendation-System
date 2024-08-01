import sqlite3

def create_database():
    conn = sqlite3.connect('nutrition.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_data (
                 id INTEGER PRIMARY KEY,
                 age INTEGER,
                 weight REAL,
                 height REAL,
                 dietary_preferences TEXT,
                 health_conditions TEXT,
                 daily_caloric_intake REAL)''')
    conn.commit()
    conn.close()

def insert_user_data(age, weight, height, dietary_preferences, health_conditions, daily_caloric_intake):
    conn = sqlite3.connect('nutrition.db')
    c = conn.cursor()
    c.execute('''INSERT INTO user_data (age, weight, height, dietary_preferences, health_conditions, daily_caloric_intake)
                 VALUES (?, ?, ?, ?, ?, ?)''', 
              (age, weight, height, dietary_preferences, health_conditions, daily_caloric_intake))
    conn.commit()
    conn.close()

create_database()
# Example of inserting data
insert_user_data(25, 70.5, 175, 'vegan', 'none', 2500)
