class Person(object):
    def __init__(self,first,last,age):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.person = "From Person class"

    def displayDetails(self):
        print(self.firstname+" "+self.lastname+" is of age"+str(self.age))

class Employee(Person):
    def __init__(self, first, last, age,staffno):
        super().__init__(first, last, age)
        self.staffnumber = staffno
        self.employee = "From Employee class"

    def displayDetails(self):
        print(self.firstname+" "+self.lastname+", "+str(self.age)+","+str(self.staffnumber))

    def displayEmployeeSalary(self,basic=None,hra=None):
        if hra==None:
            print("Basic:",basic)
        else:
            print("Basic+hra:",basic+hra)


if __name__ == "main":
    x = Person("Thomas","Shelby",50)
    y = Employee("Sheldon","Cooper",30,"0007")
    print(x.pmsg)
    x.displayDetails()
    print("-----------------------")
    print(y.emsg)
    y.displayDetails()

    y.displayEmployeeSalary(50000)
    y.displayEmployeeSalary(50000,3500)

