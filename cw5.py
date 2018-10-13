bazaAuto = ["Polonez","Mazda","Subaru","Kamaz","Jelcz","Autosan"]

while True:
	mamyTo = 0
	szukaneAuto = raw_input("Wprowadz samochod ktorego szukasz: ")

	for auto in bazaAuto:
		if auto == szukaneAuto:
			mamyTo = mamyTo + 1;
 
	if mamyTo > 0:	
		print("Mamy auto " + szukaneAuto)
	else:
		print("Niestety nie mamy tego auta")


