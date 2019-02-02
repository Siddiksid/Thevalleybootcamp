class pen:

	def __init__(self,color,length,material):
		self.color=color
		self.length=length
		self.material=material

	def change_color(self,color):
		self.color=color
   
	def __add__(self,other):
		return pen(self.color, self.length + other.length, other.material)

reynolds=pen('green',25,'plastic')
fc=pen('black',12,'metal')
camel=reynolds+fc
print(camel.color,camel.length,camel.material)
#reynolds.change_color('black')
#reynolds.change_length(24)
#print(reynolds.color,reynolds.len,reynolds.mat)