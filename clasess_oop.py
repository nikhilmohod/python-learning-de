print("clasee with oop")

class project():
    prj_name = "dummy"
    items =10

    def details(self,prj_name = prj_name,items=items): # 'self' imp keyword
        basic ="catalog"
        print(f"function called : {basic}")
        print(f"call attribute called {self.prj_name} and {self.items}")  # 'self' imp keyword
        print(f"call attribute called {prj_name} and {items}")  # with inner parameter not from class


prj = project()
print(prj.items)
prj.details()
prj.details('UC',2)


print("constructor")

class employee():

    company_name ="ABC" # class attribute - constant

    # def __init__(self):
    #     print("constructor called")

    def __init__(self,emp_name,emp_dept): # instance attribute
        self.emp_name = emp_name
        self.emp_dept = emp_dept
        print("constructor called -2")

    def details(self):
        print(f"Employee {self.emp_name} and {self.emp_dept} from {self.company_name}")  # 'self' imp keyword
    

# emp=employee()
emp=employee('nik','AV')
emp.details()