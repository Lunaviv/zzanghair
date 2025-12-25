class Designer:   
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def show(self):
        print(self.name, self.age, self.sex, sep=' ') 

class DesignerManager:
    def __init__(self):
        self.designers = []
    
    def add(self, designer):
        self.designers.append(designer)
    
    def show(self):
        for designer in self.designers:
            designer.show()
    
    # update
    # delete