from animal import Animal 							


class person(Animal):

	def __init__(self,name,age,height,weight,color,job,school,university):
		Animal.__init__(self,name,age,height,weight,color)
		self.university=university
		self.job=job
		self.school=school
		self.friends=[]
	def get_university(self):
		return self.university

	def set_university(self,newuniv):
		self.university=newuniv

	def get_job(self):
		return self.job

	def set_job(self,newjob):
		self.job=newjob

	def get_school(self):
		return self.school

	def set_school(self,newschool):
		self.school=newschool

	def get_friends(self):

		return self.friends

	def speak(self):
		print("hello")

	def add_friend(self,fname):
		if fname not in self.friends:
			self.friends.append(fname)

	def age_diff(self,other):
		diff=self.age-other.age
		print(abs(diff),"year difference")

	def __str__(self):
		return "person:"+str(self.name)+":"+str(self.age)+":"+str(self.job)

siddik=person('siddik',21,6.1,75,'blue','student','vijay vidyalaya','anna university')

print(siddik.get_name())
siddik.set_name('sid')
print(siddik.get_name())


