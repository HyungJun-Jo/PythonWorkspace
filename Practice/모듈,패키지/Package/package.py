import travel.thailand      # import는 모듈이나 패키지만 가능함. 클래스나 함수는 불가능 
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import *        # * 을 정의해서 사용하기 위해서는 공개범위를 __init__.py 에 __all__ 을 정의해줘야 사용 가능하다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()
