
import pickle

# 쓰기
profile_file = open("practice\입출력\profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프" "코딩"]}
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

# 읽기
profile_file = open("practice\입출력\profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()