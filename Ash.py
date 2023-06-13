class Ash:
    def __init__ (self,name,major,gpa):
       self.name = name
       self.major = major
       self.gpa = gpa
  
    def Is_better(self):
        if self.gpa >= 30:
            return True
        else :
            return False    
