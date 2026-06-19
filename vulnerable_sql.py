# vulnerable_sql.py
import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")

    # 취약점: 사용자 입력을 직접 SQL에 삽입
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor = conn.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print(get_user(input("Username: ")))
