def doubler(func):
	def wrapper():
		function2 = func()
		function1 = func()
	return wrapper 
