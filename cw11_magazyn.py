import csv
# import pprint

def calculate_cost(ilosc, cena):
	return ilosc*cena

def calculate_mass(ilosc, masa):
	return ilosc*masa

def save_to_file(plik, tekst):
	file = open(plik,"w")
	file.write(tekst +"\n")

def append_to_file(plik, tekst):
	file = open(plik, "a")
	file.write(tekst + "\n")
	file.close()


def main():

	magazyn = [{"nazwa": "sruba", "ID": "0151","masa": 0.1, "ilosc": 16, "cena": 2.25, "isToxic": True},
		   {"nazwa": "nakretka", "ID": "2667", "masa": 0.05, "ilosc": 45, "cena": 0.7, "isToxic": False},
		   {"nazwa": "podkladka", "ID": "3553", "masa": 0.01, "ilosc": 124, "cena": 0.2, "isToxic": False},
		   {"nazwa": "pin", "ID": "1667", "masa": 0.015, "ilosc": 325, "cena": 1, "isToxic": True},
		   {"nazwa": "insert", "ID": "3764", "masa": 0.75, "ilosc": 50, "cena": 14, "isToxic": True},
		   {"nazwa": "zlacze", "ID": "0021", "masa": 1, "ilosc": 7, "cena": 65, "isToxic": False},
		   {"nazwa": "blacha", "ID": "0008", "masa": 3.5, "ilosc": 2, "cena": 88},
		   {"nazwa": "nit", "ID": "9210", "masa": 0.15, "ilosc": 19, "cena": 0.5, "isToxic": True}]


#CO ZROBIC JAK  JEDEN ZE SLOWNIKOW NIE MA DANEGO KLUCZA?

		#i = 0
		#tekstDoPliku = "Produkt " + pozycja["nazwa"] + " jest dostepny w ilosci " + str(pozycja["ilosc"])+ " sztuk ktore razem waza " + str(calculate_mass(pozycja["ilosc"], pozycja["masa"])) + " kg i kosztuja " + str(calculate_cost(pozycja["ilosc"], pozycja["cena"])) + " EUR"
		#print(tekstDoPliku)
		#if i == 0:
		#	save_to_file("produkty.txt",tekstDoPliku)
		#else:
		#	append_to_file("produkty.txt", tekstDoPliku)
		#i = i+1
	totalIlosc = 0
	totalMass = 0
	totalCost = 0
	totalToxic = 0
	totalNonToxic = 0

	for atrybut in magazyn:
		totalIlosc = totalIlosc + atrybut["ilosc"]
		totalMass = totalMass + calculate_mass(atrybut["ilosc"], atrybut["masa"])
		totalCost = totalCost + calculate_cost(atrybut["ilosc"], atrybut["cena"])
		if "isToxic" in atrybut and  atrybut["isToxic"] == True:
				totalToxic = totalToxic + atrybut["ilosc"]
		elif not("isToxic" in atrybut) or atrybut["isToxic"] == False:
				totalNonToxic = totalNonToxic + atrybut["ilosc"]


	print("Calkowita ilosc towarow na magazynie wynosi " +  str(totalIlosc))
	print("Calkowita masa towarow na magazynie wynosi " + str(totalMass))
	print("Calkowity koszt towarow na magazynie wynosi" + str(totalCost))
	print("Ilosc materialow toksycznych: " + str(totalToxic))
	print("Ilosc materialow nietoskycznych: " +str(totalNonToxic))
	textVal = "Calkowita masa," + str(totalMass) + ",Calkowita ilosc," + str(totalIlosc) + ",Calkowity koszt," + str(totalCost) + ",Ilosc toksycznych," + str(totalToxic) + ",Ilosc nietoksycznych," + str(totalNonToxic)

	save_to_file("produkty.csv", textVal)


#TODO
#odczyt z csv

if __name__ == "__main__":
	main()
