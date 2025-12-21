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
    global currentPage
    currentPage = "Home"
    global numberOfOptions
    numberOfOptions = 4
    print("---------------------------------------------------")
    greeting = """안녕하세요 원장님 짱헤어입니다. \n무엇을 도와드릴까요?"""
    print(greeting)
    menu = """디자이너[1], 고객[2], 결제내역[3], 서비스[4]"""
    print(menu)
    match checkInput():
        case 1:
            designerMenu()
        case 2:
            clientMenu()
        case 3:
            caseMenu()
        case 4:
            serviceMenu()
        case _:
            print("없는 메뉴입니다. 홈으로 돌아갑니다.")
            home()
    
options = "추가[1], 수정[2], 삭제[3], 홈으로[4]"
currentPage = "Home"
designerList = []
clientList = []
caseList = []
serviceList = []
numberOfOptions = 0

def menu():
    global numberOfOptions
    numberOfOptions = 4

def designerMenu():
    menu()
    global currentPage 
    currentPage = "디자이너 목록"
    print(currentPage)
    showList()
    print(options)
    memuInput(checkInput())

def clientMenu():
    menu()
    global currentPage 
    currentPage = "고객 목록"
    print(currentPage)
    showList()
    print(options)
    memuInput(checkInput())

def caseMenu():
    menu()
    global currentPage 
    currentPage = "결제내역"
    print(currentPage)
    showList()
    print(options)
    memuInput(checkInput())

def serviceMenu():
    menu()
    global currentPage 
    currentPage = "서비스 목록"
    print(currentPage)
    showList()
    print(options)
    memuInput(checkInput())

def checkInput(): #모든 메뉴에서 재사용할 사용자 인풋 검사기. 
    y = True
    while y == True:
        x = input()
        try:
            x = float(x);
            y = False
        except:
            print("입력내용을 다시 확인해주세요")
    return x

def memuInput(x): #C_UD 통합 시도
        match x:
            case 1:
                print("추가")
                add()
            case 2:
                print("수정")
                add()
            case 3:
                print("삭제")
                add()
            case 4:
                home()
            case _:
                print("없는 메뉴입니다. 홈으로 돌아갑니다.")
                home()

def add():
    match currentPage:
        case "디자이너 목록":
            print("디자이너 추가")
            name = input("이름을 입력해주세요")
            age = input("나이를 입력해주세요.")
            sex = input("성별을 입력해주세요.")
            designerList.append(Designer(name, age, sex))
            print("추가가 완료되었습니다. 홈으로 돌아갑니다.")
            home()
        case "고객 목록":
            print("고객 추가")
            name = input("이름을 입력해주세요")
            age = input("나이를 입력해주세요.")
            sex = input("성별을 입력해주세요.")
            clientList.append(Client(name, age, sex))
            print("추가가 완료되었습니다. 홈으로 돌아갑니다.")
            home()
        case "결제내역":
            print("결제내역 추가")
            designer = input("디자이너 이름을 입력해주세요")
            client = input("고객 이름을 입력해주세요.")
            price = input("금액을 입력해주세요.")
            date = input("날짜를 입력해주세요. (YYMMDD)")
            caseList.append(Case(designer, client, price, date))
            print("추가가 완료되었습니다. 홈으로 돌아갑니다.")
            home()
        case "서비스 목록":
            print("서비스 추가")
            name = input("서비스 이름을 입력해주세요")
            price = input("가격을 입력해주세요.")
            serviceList.append(Service(name, price))
            print("추가가 완료되었습니다. 홈으로 돌아갑니다.")
            home()

def showList():
    if currentPage == "디자이너 목록":
        for obj in designerList:
            print(obj.name, obj.age, obj.sex, sep=' ')
    elif currentPage == "고객 목록":
        for obj in clientList:
            print(obj.name, obj.age, obj.sex, sep=' ')
    elif currentPage == "결제내역":
        for obj in caseList:
            print(obj.designer, obj.client, obj.price, obj.date, sep=' ')
    elif currentPage == "서비스 목록":
        for obj in serviceList:
            print(obj.name, obj.price, sep=' ')


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