class Animal(object):
	def __init__(self,name,age,height,weight,color):
		self.age=age
		self.name=name
		self.height=height
		self.weight=weight
		self.color=color
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_name(self,newname=" "):
		self.name=newname
	def set_age(self,age):
		self.age=age
	def __str__(self):
		return "animals:"+str(self.age)+":"+str(self.name)
	def who_is_this(self):
		print("this is panda")

john=Animal('john',15,6,300,'green')


