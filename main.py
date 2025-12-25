from components.client import Client,ClientManager
# from components.designer import

def showClient():
    ClientManager.show()

#
def addClient():
    #ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
    newClient = Client(name, age, sex)
    name = input("name: ")
    age = input("age: ")
    sex = input("sex: ")
    
    ClientManager.add(newClient)
    
def main():
    print("미용실CRM")
    cmd = input(">>")
    error = "없는 메뉴입니다. help로 메뉴 목록을 확인하세요."
    clientManager = ClientManager()
    
    #고객CRUD
    if cmd == "addc":
        print("고객추가")
        addClient()
        main()
    elif cmd == "readc":
        print("고객목록")
        ClientManager.show()
        main()
    elif cmd == "updc":
        print("고객수정")
    elif cmd == "delc":
        print("고객삭제")
    else:
        print(error)
        main()


main()