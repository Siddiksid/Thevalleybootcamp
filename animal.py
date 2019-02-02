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

	def get_height(self):
		return self.height

	def get_weight(self):
		return self.weight

	def get_color(self):
		return self.color

	def set_height(self,newheight):
		self.height=newheight

	def set_weight(self,newweight=0):
		self.weight=newweight

	def set_color(self,newcolor):
		self.color=newcolor

	def __str__(self):
		return "animals:"+str(self.age)+":"+str(self.name)
	




