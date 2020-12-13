# 모듈을 사용하려면 같은 폴더 경로에 있거나, 해당 경로를 지정해줘야한다.
# 아래 예제는 같은 폴더 경로에 있다고 가정하고 작성

import module_theater as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


from module_theater import *
price(3)
price_morning(4)
price_soldier(5)


