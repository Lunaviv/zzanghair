from utils.database import Database

class Client:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        print(self.name, self.age, self.sex, sep = " ")


class ClientManager:
    def __init__(self):
        self.db = Database()
        self.clients = []
        self.load()
        
    def load(self):
        data = self.db.load()
        for i in range(0, len(data), 3):
            name = data[i]
            age = int(data[i+1])
            sex = data[i+2]
            self.clients.append(Client(name, age, sex))

    def add(self, client):
        self.clients.append(client)
        self.db.save(self.clients)

    def show(self):
        self.db.load()
        for client in self.clients:
            client.show()

    def count(self):
        return len(self.clients)

    def update(self, n, updatedClient):
        self.clients[n] = updatedClient
        self.db.save(self.clients)

    def delete(self, n):
        self.clients.pop(n)
        self.db.save(self.clients)
    
    def clear(self):
        self.db.clear()


'''
class ClientManager:
    def __init__(self):
        self.clients = []

    def add(self, client):
        self.clients.append(client)

    def show(self):
        for client in self.clients:
            client.show()

    def count(self):
        return len(self.clients)

    def update(self, n, updatedClient):
        self.clients[n] = updatedClient

    def delete(self, n):
        self.clients.pop(n)
'''