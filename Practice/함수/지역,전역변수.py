
gun = 10  #전역번수

def checkpoint(soldiers):
    global gun             # 전역공간에 있는 gun(전역번수 사용)
    gun_local = 5          # 지역변수
    gun = gun - gun_local - soldiers    # 10-5-2

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)      # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 2)            # 3-2
print("남은 총 : {0}".format(gun))