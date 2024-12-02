accend = False

with open("test.txt","r") as file:
	for i in file:
		values = i.split()
		print(i.split())
		for n in range(len(values)):
			if n == len(values):
				print("end")
			elif values[n] > values[n+1]:
				print("dec",values[n],n,len(values))
			elif values[n] < values[n+1]:
				print("acc",values[n],n,len(values))
			else:
				print("invalid")
