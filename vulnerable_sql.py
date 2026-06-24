import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL injection: 사용자 입력이 쿼리에 직접 삽입됨
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    user_input = input("Enter username: ")
    results = get_user(user_input)
    print(results)

if __name__ == "__main__":
    main()
