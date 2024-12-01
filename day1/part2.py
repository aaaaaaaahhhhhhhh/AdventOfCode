list1 = []
list2 = []
list3 = []
with open("input.txt","r") as file:
	lines = file.readlines()

for i in lines:
	values = i.split()
	temp = values[0]
	counter = 0
	for n in lines:
		values = n.split()
		if temp == values[1]:
			counter += 1

	list3.append(counter*int(temp))
print(sum(list3))

