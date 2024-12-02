counter = 0

def AorD(values):
	if sorted(values) == values or sorted(values, reverse=True) == values:
		return True
	return False
def OneToThree(values):
	for n in range(len(values)-1):
		if not (1 <= (abs(values[n]-values[n+1])) <= 3):
			return False
	return True

with open("input.txt","r") as file:
	for i in file:
		values = list(map(int, i.split()))
		if AorD(values) and OneToThree(values):
			counter += 1
	print(counter)
