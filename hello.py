import datetime

def hello():
	print('创建一个版本')

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name
	
	def say(self):
		print("hello word!")
		
