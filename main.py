from components.client import Client, ClientManager
from components.designer import Designer, DesignerManager

def addClient(clientManager):
    pass

def main():
    clientManager = ClientManager()

    cmd = input(">> ")
    if cmd == "addc":
        addClient(clientManager)

if __name__ == '__main__':
    main()