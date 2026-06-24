# vulnerable_path.py  
import os
import sys

user_file = sys.argv[1]  # 외부 입력
path = "/var/data/" + user_file
with open(path) as f:  # CodeQL py/path-injection 감지 포인트
    print(f.read())
