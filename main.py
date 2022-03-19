import time

def decor(foo):

	def new_foo(*args, **kwars):
		parametres = []
		parametres.append(time.ctime())
		result = foo(*args, **kwars)
		parametres.append(f'{foo.__name__}')
		parametres.append(args)
		parametres.append(result)
		with open('log.txt', 'w', encoding='UTF-8') as f:
			f.write(f'{parametres}')
		return result

	return new_foo

@decor
def function(a, b):
	x = a + b
	print(x)
	return x

function(2, 4)