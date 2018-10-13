def wypiszLitereSamochodu(literaOdKonca, tablicaSamochodow):
	for samochod in tablicaSamochodow:
		if len(samochod)-literaOdKonca > 0:
			print(samochod[len(samochod)-literaOdKonca])
		elif len(samochod) == 0:
			print("BLAD: Pusty ciag znakow")
		else:
			print("Dana marka nie ma tylu liter w nazwie")

samochody = ["Polonez", "Honda", "Peugeot", "kia"]

wypiszLitereSamochodu(5,samochody)
