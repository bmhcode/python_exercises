class Employee:
    def __init__(self, name, date_beirth, grade ):
        self.name  = name
        self.date_beirth = date_beirth
        self.grade = grade
    
    def get_age(self):
        return 2024 - self.date_beirth

empl = Employee('Bouraghda Mohamed Elhadi', 1976, "Software Engeneer")
print(empl.name)
print(empl.get_age())

list_employes = []
while True:
    name = input("Tap your name : ")
    list_employes.append(name)
    if name == "q" or name == "Q":
        exit()
        
for empl in list_employes:
    print(empl,end='|')
  
        
        