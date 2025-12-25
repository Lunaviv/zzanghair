class Client:   
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def show(self):
        print(self.name, self.age, self.sex, sep=' ') 

class ClientManager:
    def __init__(self):
        self.clients = []
    
    def add(self, client):
        self.clients.append(client)
    
    def show(self):
        for client in self.clients:
            client.show()
    
    # update
    # delete