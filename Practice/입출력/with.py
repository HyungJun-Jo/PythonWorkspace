# 파일입출력시에 문장을 짧게 쓰기 위해 with 사용

with open("Practice\입출력\study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")


with open("Practice\입출력\study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())