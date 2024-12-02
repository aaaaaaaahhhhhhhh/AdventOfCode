counter = 0
with open("input.txt","r") as file:
	for i in file:
		values = list(map(int, i.split()))
		level = 1
		if sorted(values) == values or sorted(values, reverse=True) == values:
			for n in range(len(values)-1):
				if not (1 <= (abs(values[n]-values[n+1])) <= 3):
					break
			else:
				counter += 1
			
print(counter)
