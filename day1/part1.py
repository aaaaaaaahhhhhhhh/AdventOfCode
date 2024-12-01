list1 = []
list2 = []
list3 = []
with open("input.txt","r") as file:
	for i in file:
		values = i.split()
		for i in range(0,2):
			if i == 0:
				list1.append(values[i])
			else:
				list2.append(values[i])
list1.sort()
list2.sort()
for i in range(len(list1)):
	list3.append(abs(int(list1[i]) - int(list2[i])))

print(sum(list3))



