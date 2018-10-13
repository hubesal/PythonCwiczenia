samochody = ["Jelcz", "Autosan", "Mazda", "Subaru", "Polonez", "Maluch"]
spalanie = [25.5, 27.6, 8.0, 11.0, 10.1, 7.5]
koszt_paliwa = 4.5

while True:

	auto = raw_input("Podaj nazwe auta: ")
	przejechaneKm = raw_input("Podaj liczbe przejechanych km: ")
	spalanieWybranego = samochody.index(auto)
	koszt = koszt_paliwa*(spalanie[spalanieWybranego]/100.0)*float(przejechaneKm)
	print("Koszt przejechanych " + str(przejechaneKm) + " kilometrow wynosi " + str(koszt) + " PLN")
