counter = 0
with open("input.txt","r") as file:
	for i in file:
		values = i.split()
		counter += 1
		if sorted(values) == values or sorted(values, reverse=True) == values:
			for n in range(len(values)-1):
				if abs(int(values[n])-int(values[n+1])) >= 1 and abs(int(values[n])-int(values[n+1])) <= 3:
					true = True
				else:
					counter -= 1
					break


		else:
			counter -= 1
print(counter)


