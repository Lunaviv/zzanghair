class Client:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        print(self.name, self.age, self.sex, sep = " ")

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