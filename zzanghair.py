"""[필요 클래스]

① 직원 클래스
- 직원 정보 관리

② 고객 클래스
- 고객 정보 관리

③ 직원-고객 클래스 (이름 지어줘)
- 어떤 직원이 어떤 고객에게 어떤 서비스를 했는지

④ 서비스 클래스 (이름 지어줘)
- 가격 정보 등등

[필요 기능 = CRUD]
- 위 클래스들에 대한 Create / Read / Update / Delete 기능
- UI는 아무렇게나 text-based로!

저장은 list로 하자 우선 영구저장 X

이거 기반으로 하나씩 기능을 추가해가면 될듯?

1. file io 부터 추가하고 나중에 이거 db로 바꿔보고
2. text ui를 graphical ui로 바꿔보고
3. 네트워크 기능 추가하고 등등
"""

def home():
    greeting = """안녕하세요 원장님 짱헤어입니다. \n무엇을 도와드릴까요?"""
    print(greeting)
    menu = """디자이너[0], 고객[1], 결제내역[2], 서비스[3]"""
    print(menu)


class Designer:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Client:   
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Case:
    def __init__(self, designer, client, price, date):
        self.designer = designer
        self.client = client
        self.price = price
        self.date = date

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

home()