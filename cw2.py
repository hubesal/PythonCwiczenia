samochody = ['syrena','polonez']

for x in samochody:
	print(x)

for idx in range(len(samochody)):
	print("index " + str(idx) + ": " + samochody[idx])

# print(samochody[2]) --> index out of range (NullPointerException w javie)
