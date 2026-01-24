import os

class Database:
    def __init__(self, file="clients.data"):
        self.file = file

    def save(self, clientList):
        with open(self.file, "w") as f:
            for c in clientList:
                line = f"{c.name}\n{c.age}\n{c.sex}\n"
                f.write(line)

    def load(self): #raw to list
        if not os.path.exists(self.file):
            return []
        with open(self.file, "r") as f:
            return [line.strip() for line in f.readlines()]
                
    def clear(self):
        if os.path.exists(self.file):
            os.remove(self.file)

