
score_file = open("practice\입출력\score.txt", 'w', encoding="utf8")  # 한글이 꺠지는 경우가 있기 때문에 uft8 인코딩 권장
print("수학 : 0", file=score_file)
print("영어 : 50" , file=score_file)
score_file.close()

score_file = open("practice\입출력\score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.close()


score_file = open("practice\입출력\score.txt", "r", encoding="utf8")
print(score_file.read())        # 텍스트 파일 읽어오기
score_file.close()
print("\n")

score_file = open("practice\입출력\score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()   # 텍스트 한줄씩 불러오기 
    if not line:
        break
    print(line, end="")
score_file.close()
print("\n")

score_file = open("practice\입출력\score.txt", "r", encoding="utf8")
lines = score_file.readlines()    # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print("\n")
