bazaSamochodow = {'Polonez': '11.0', 'Ursus': '25.0', 'Autosan': '21.5', 'Golf': '8.2'}
cenaPaliwa = 4.5

for key, value in bazaSamochodow.iteritems():
	print("spalanie samochodu {0} wynosi {1} l na 100km".format(key, value))

