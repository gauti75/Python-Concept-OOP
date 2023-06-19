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



