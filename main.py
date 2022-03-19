


def decor(foo):
	def new_foo(*args, **kwars):
		parametres = []
		result = foo(*args, **kwars)

		return result

	return new_foo