
def OneToThree(values):
	k = 0
	error = 0
	while k < len(values)-1:
		diff = abs(values[k]-values[k+1])
		if not (1 <= diff <= 3):
			values.pop(k)
			error += 1
		else:
			k += 1
	return error


#def OneToThree(values):
#	new_list = values[:]
#	print(new_list) #
#	error = 0
#	for n in range(len(new_list)-1):
#		diff = abs(new_list[n]-new_list[n+1])
#		if not (1 <= diff <= 3):
#			error += 1
#	return error

def deccending(values):
	new_list = values[:]
	i = 0
	error = 0
	while i < len(new_list)-1:
		if new_list[i] > new_list[i+1]:
			i += 1
		else:
			new_list.pop(i)
			if i > 0:
				i -= 1
			error += 1
	return error

def accending(values):
	new_list = values[:]
	i = 0
	error = 0

	while i < len(new_list)-1:
		if new_list[i] < new_list[i+1]:
			i += 1
		else:
			new_list.pop(i)
			error += 1
	return error

counter = 0

def part1(a, d, t):
	if a == 0 and t == 0:
		return 1
	elif d == 0 and t == 0:
		return 1
	else:
		return 0

def part2(a, d, t):

	adt = [a,d,t]
	if adt.count(0) == 1 and adt.count(1) == 1:
		print("SUC")

		return 1
	return 0

counter2 = 0

with open("test2.txt","r") as file:
	for i in file:
		my_list = list(map(int, i.split()))
		t = OneToThree(my_list[:])

		a = accending(my_list[:])
		d = deccending(my_list[:])
		print(f"a {a} d {d} t{t}")

		if part1(a,d,t):
			counter += 1
		else:
			counter2 += part2(a,d,t)



	print("safe paths for part 1", counter)
	print("safe paths for part 2", counter2)
#		if AorD(values) and OneToThree(values):
#			counter += 1
#	print(counter)
