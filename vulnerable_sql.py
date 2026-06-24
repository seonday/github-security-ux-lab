# vulnerable_sql.py
import sqlite3
import sys

conn = sqlite3.connect(':memory:')
conn.execute("CREATE TABLE users (id INTEGER, name TEXT, password TEXT)")

username = sys.argv[1]  # 외부 입력
query = "SELECT * FROM users WHERE name = '" + username + "'"
conn.execute(query)
