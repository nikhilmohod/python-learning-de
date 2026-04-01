class employee():

    company_name ="ABC" # class attribute - constant


    def __init__(self,emp_name,emp_dept): # instance attribute
        self.emp_name = emp_name
        self.emp_dept = emp_dept
        print("constructor called -2")

      # Static methods - this top method run before everything static
    @staticmethod
    def Company_details(company_name):
        print(f"Company Name : {company_name}")  


    # Instance methods - ue are calling it using class instance
    def details(self):
        print(f"Normal Method : Employee {self.emp_name} and {self.emp_dept} from {self.company_name}")  # 'self' imp keyword

     # Class methods - ue are calling it using class instance but with class decorator
    @classmethod
    def details_info(cls,emp_name,emp_town):
        print(f"Class Method : Employee {cls.emp_name} and {cls.emp_town} from {self.company_name}")  # 'self' imp keyword

    print("Getter and Setter") # to get instace attribute value and setter to set

    @property #getter
    def emp_info(self):
        print(f"Normal Method : Employee {self.emp_name} and {self.emp_dept} from {self.company_name}")  # 'setting the value

    @emp_info.setter
    def emp_info(self ,emp_dt):
        self.emp_name = emp_dt[0]
        self.emp_dept = emp_dt[1]



emp=employee('nik','AV')
emp.Company_details("Clouda")
emp.details()
emp.Company_details('Pune')
emp.emp_info = ['nik-1','ABC']
print(emp.emp_info)




