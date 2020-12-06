#키워드 검색 기능을 사용하지 않은 엑셀파일에서 특정 키워드를 찾기 위해 만든 코드
import csv

file = input("파일 이름을 입력하세요(.csv 확장자 포함) : ")
keyword = input("키워드를 입력하세요 : ")
cnt = 0
line = 1
#csv 파일 열기
with open(file, 'r') as f:
    reader = csv.reader(f)
    print("키워드가 등장하는 기사 번호 : ")
    for txt in reader:
        #csv파일의 각 줄에서 원하는 키워드 찾기
        if txt[4].find(keyword) != -1:
            print(line)
            cnt += 1
        line += 1
print("키워드가 등장하는 기사의 개수 : ", cnt)
