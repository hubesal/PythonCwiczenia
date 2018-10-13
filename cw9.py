koty = ["Pimpus","Mruczek"]

while True:
	czyChcesz = raw_input("Chcesz kolejnego kota? ")
	if czyChcesz == 'Yes':
		imieNowego = raw_input("Wprowadz jego imie: ")
		koty.append(imieNowego)
	elif czyChcesz == 'No':
		for kot in koty:
			print(kot)
		break
	else:
		print("Nie rozumiem")
