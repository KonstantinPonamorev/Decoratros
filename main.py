import time

def decor_path(path=str):
	def decor(foo):
		def new_foo(*args, **kwars):
			parametres = []
			parametres.append(time.ctime())
			result = foo(*args, **kwars)
			parametres.append(f'{foo.__name__}')
			parametres.append(args)
			parametres.append(result)
			with open(f'{path}log.txt', 'w', encoding='UTF-8') as f:
				f.write(f'{parametres}')
			return result
		return new_foo
	return decor


@decor_path('')
def function(a, b):
	x = a + b
	print(x)
	return x


if __name__ == '__main__':
	function(2, 4)