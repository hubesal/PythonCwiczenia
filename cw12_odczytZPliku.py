import pprint
def fileRead(plik):
	file = open(plik, "r");
	tekst = file.read();
	print(tekst);
	file.close();

def fileWrite(table):

	for zw in table:
		file.write(zw + "\n");
	file.close()


zwierzeta = ["Kot","Pies","Chomik","Rybki"]
tabLength = len(zwierzeta);

file = open("zwierzeta.txt", "w");
fileWrite(zwierzeta);
fileRead("zwierzeta.txt");

while True:
	nowe = raw_input("Chcesz dodac kolejne zwierze? Jesli tak, to jakie? Jesli nie , wpisz 'nie'")
	if not(nowe == "nie"):
		zwierzeta.append(nowe);
		tabLength = len(zwierzeta);

	else:
		break

file = open("zwierzeta.txt","a")
for zw in zwierzeta[tabLength: len(zwierzeta)]:
	file.write(zw +"\n");
file.close();

fileRead("zwierzeta.txt")
pprint.pprint(zwierzeta)

#TODO
#czemu nie zapisuje do tekstu
