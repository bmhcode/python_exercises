class Personne:
    def __init__(self, first_name, last_name, beirth_year):
        self.first_name  = first_name
        self.last_name  = last_name
        self.beirth_year = beirth_year
        # self.grade = grade
        # self.notes = []
        
    @property       
    def full_name(self, first_name, last_name):
        return f'{self.first_name} {last_name}'
        
    @full_name.setter        
    def full_name(self, name):
        self.last_name, self.last_name = name.split()
           
    @property 
    def get_age(self):
        return 2024 - self.beirth_year

    def add_note(self):
        for note in self.notes:
            self.notes.append(note)
            
fname,lname = str(input("Tap your name : ")).split()
year = int(input ('Enter your year of beirthday : '))
   
employe = Personne(fname,lname,year)
# employe.full_name = "Bouraghda"
print(employe.full_name(fname,lname)," | ",employe.get_age)
   

        
        