from components.client import Client,ClientManager 


def archive(): #온전히 컬러코딩만을 위한 함수

    #1 인스턴스 수동생성
    c1 = Client("이주안", 27, "M")
    c2 = Client("이호성", 28, "M")
    c3 = Client("하석훈", 27, "M")

    cman = ClientManager() #맴니저 호출 인스턴시에으트를 해야만 다룰 수 있다.

    cman.add(c1)
    cman.add(c2)
    cman.add(c3)

    #2 인스턴스 변수받아서 생성
    name = "하석훈"
    age = 27
    sex = "M"
    c4 = Client(name, age, sex)
    
    cman.add(c4)

    #3 인스턴스 인풋받아서 생성
    inputName = input("name: ")
    inputAge = input("age: ")
    inputSex = input("sex: ")
    c5 = Client(inputName, inputAge, inputSex)
    cman.add(c5)

    cman.show()