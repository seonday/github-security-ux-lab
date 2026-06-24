import os

def read_file(filename):
    # Path injection: 사용자 입력이 파일 경로에 직접 사용됨
    base_dir = "/var/data/"
    file_path = os.path.join(base_dir, filename)
    with open(file_path, 'r') as f:
        return f.read()

def main():
    user_input = input("Enter filename: ")
    content = read_file(user_input)
    print(content)

if __name__ == "__main__":
    main()
