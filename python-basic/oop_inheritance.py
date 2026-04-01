print("inheritance") # aquire property or use method or property from pratent class


#c parent class
class school():

    def __init__(self,s_name):
        self.s_name = s_name
        print(f"school name : {self.s_name}")


    def school_info(self,s_name):
        print("parent md call")

        print(f"school name : {s_name}")
    
    def whoAmI(self):
        print("school")


# child class
class teacher(school): # inheri school

    def __init__(self,t_name,s_name):
        self.t_name = t_name
        school.__init__(self ,s_name) # 1. usi this or blow 
        self.s_name = s_name # this another way for above
        print(f"teacher name {self.t_name} and school {self.s_name} ")

    def teacher_info(self,t_name):
        print("teacher func calling .....")
        print(f"teacher name : {t_name}")
        school.school_info(self,self.s_name) #1. usi this or below using super()
        super().school_info(self.s_name) # using super() - self keyword not required

    def whoAmI(self):
        print("teacher")

class student(teacher): # multi level school -> teacher - > student
    
    def __intit__(self, t_name,s_name):
        print("student constructore")
        teacher.__init__(self,self.s_name)

    def student_info(self,st_name):
        teacher.teacher_info(self,self.t_name)
        print(f"student name {st_name}")

    def whoAmI(self): # if same method available then priority will be calling object then 2nd so on
        print("student")



# sc = school()
# sc.school_info("HCJ")
# tc = teacher("HCJ-2","nik-2")
# tc.school_info("HCJ-3") # using school method using teacher object
# tc.teacher_info("rahul")

st = student("gajanan","abc")
st.student_info("mohan")
st.whoAmI() # same method

sc = school("HCJ")
sc.whoAmI()  # same method
