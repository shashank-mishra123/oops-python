#Demonstrat the multi level inheritance 
# Person-> Employee->Maneger
class Person:
    def __init__(self):
       print("i am a person")
    
    def speaking(self):
        print(" speaking in -> hindi ,-> english")

    def walking(self):
        print(" walking  and riding also ")

class Employee(Person):
    def __init__(self):
        print(" I am a Employee")
    
    def company_name(self):
        print("Lunteron web services")

    def employee_id(self):
        print("012Shashank&$")

class Maneger(Employee):
    def __init__(self):
        print(" I am a Maneger")
    
    def responsibilty(self):
        print(" to manege all the employee under it")

per =Person()

emp =Employee()
print(emp.speaking)
print(emp.company_name)

man = Maneger()
print(man.speaking)
print(man.responsibilty)
print(man.company_name)
print(man.employee_id)