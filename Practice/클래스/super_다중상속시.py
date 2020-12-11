class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()


dropship = FlyableUnit()   # 첫번째 상속된 Unit 클래스의 생성자만 가져온다