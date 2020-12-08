# path = "Practice\입출력\practice_파일입출력\"

for week in range(1, 51): # 1~51
    filename = "Practice\입출력\practice_파일입출력" + "\\" + str(week) + "주차.txt"
    with open(filename, "w", encoding="utf8") as meeting_minute:
        meeting_minute.write("- " + str(week) + " 주차 주간보고 -\n")
        meeting_minute.write("부서 : \n")
        meeting_minute.write("이름 : \n")
        meeting_minute.write("업무 요약 : \n")
    