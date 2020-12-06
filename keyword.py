import csv

file = input("파일 이름을 입력하세요(.csv 확장자 포함) : ")
keyword = input("키워드를 입력하세요 : ")
cnt = 0
line = 1
with open(file, 'r') as f:
    reader = csv.reader(f)
    print("키워드가 등장하는 기사 번호 : ")
    for txt in reader:
        if txt[4].find(keyword) != -1:
            print(line)
        line += 1
        cnt += 1
print("키워드가 등장하는 기사의 개수 : ", cnt)
