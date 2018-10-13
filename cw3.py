def print_slownik(e,d):
	for key in e:
		print("{0}: {1}".format(key,d[key]))

samolot = {'name': 'airbus',
	   'model': 'A330',
	   'przebieg': 15000,
	   'typ': 'pasazerski'}

print_slownik(samolot,samolot)
