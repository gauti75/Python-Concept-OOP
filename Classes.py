class Student:
	def __init__(self,name,section):
		self.name=name
		self.section=section
	
	def display(self):
		return self.name+" "+self.section





class CPP(Student):
	def __init__(self,name,section,grade):
		Student.__init__(self, name, section)
		self.grade=grade

	def display(self):
		return Student.display(self)+" "+str(self.grade)


x=CPP("gautam","nra",34)
y=Student("gautam","nra")

print(x.display())

print(y.display())



#### Another Basic Example of Python Classes  ####


print("\n\n Second Example \n\n")
class Mobile:
    model_name=None
    mfg_year=None
    camera_pixel=None

    def __init__(self,model_name,mfg_year,camera_pixel):
        self.model_name=model_name
        self.mfg_year=mfg_year
        self.camera_pixel=camera_pixel

    def display(self):
        print("This is your phone details\n")
        print("Model_name: "+self.model_name)
        print(f"Manufacturing Year: {self.mfg_year}")
        print(f"Pixel in this model: {self.camera_pixel}")

    

    
mobile_1=Mobile("Galaxy FE",2020,"64 px")

mobile_1.display()



