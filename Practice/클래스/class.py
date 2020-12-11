
class Unit:
    def __init__(self, name, hp):           # 생성자
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}".format(self.hp))

# 인스턴스
marine = Unit("마린", 40)
medic = Unit("메딕", 30)
tank = Unit("탱크", 150)

# 외부에서 변수 추가 (하지만 해당 인스턴스에만 생성되는 변수임)
wraith = Unit("레이스", 80)
wraith.clocking = True

if wraith.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith.name))

# 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):           # 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage
        print("데미지 {0}".format(self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 예제
# - 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# - 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
        .format(name, location, self.flying_speed))
        

# 다중 상속
# - 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")