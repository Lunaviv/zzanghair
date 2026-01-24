from components.client import Client,ClientManager

def addClient(cman):
    print("고객추가")
    name = input("name: ")
    age = int(input("age: "))
    sex = input("sex: ")
    newClient = Client(name, age, sex)
    cman.add(newClient)

def showClient(cman):
    cman.show()

def updateClient(cman):
    if cman.count() == 0:
        print("No Clients in the list")
    else:
        cman.show()
        updateTarget = int(input("몇번째 고객을 수정하시겠습니까?: "))-1
        newName = input("name: ")
        newAge = int(input("age: "))
        newSex = input("sex: ")
        updatedClient = Client(newName, newAge, newSex)
        cman.update(updateTarget, updatedClient)

    
def deleteClient(cman):
    cman.show()
    deleteTarget = int(input("몇번째 고객을 삭제하시겠습니까?: "))
    if deleteTarget > cman.count():
        print("No client fount in that index")
    else:
        cman.delete(deleteTarget-1)
        
def main():
    cman = ClientManager()
    while True:
        print("미용실 CRM")
        cmd = input("명령어를 입력하세요. 명령어 목록(help):")

        
        match cmd:
            case "addc":
                addClient(cman)
            case "clist":
                cman.show()
            case "cupd":
                updateClient(cman)
            case "delc":
                deleteClient(cman)
            case "clear":
                cman.clear()
            case _:
                print("없는 메뉴입니다.")
        


if __name__ == "__main__":
    main()