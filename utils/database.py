import os

def save(newClient):
    with open("clients.data", "a") as f:
        for c in newClient:
            line = f"{c.name}\n{c.age}\n{c.sex}\n"
            f.write(line)

def read():
    clients = []
    with open("clients.data", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            name = lines[i]
            age = lines[i+1]
            sex = lines[i+2]
            clients.append((name, age, sex))
    return clients

def load():
    with open("clients.data", "r") as f:
        pass
            
        
def clear():
    os.remove("clients.data")

