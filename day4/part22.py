with open("input.txt") as fh:
	data = [l.strip() for l in fh.read().strip().splitlines()]
ops = [
	((0,0),(1,0),(2,0),(3,0)),
	((0,0),(0,1),(0,2),(0,3)),
	((0,0),(1,1),(2,2),(3,3)),
	((0,3),(1,2),(2,1),(3,0)),
]
def is_match(data, y, x):

	def is_match_op(op):
		accum = []
		for dy, dx in op:
			if y + dy == len(data) or x + dx >= len(data[y + dy]):
				return 0
			accum.append(data[y + dy][x + dx])
		return 1 if ''.join(accum) in ('XMAS', 'SAMX') else 0
	return sum(is_match_op(op) for op in ops)

def is_x_mas(data, y, x):
	if y + 2 >= len(data) or x + 2 >= len(data[y]):
		return 0
	chars = [
		(data[y][x], data[y + 2][x], data[y][x + 2], data[y + 2][x + 2]),
		(data[y][x], data[y][x + 2], data[y + 2][x], data[y + 2][x + 2]),
	]
	for c1, c2, c3, c4 in chars:
		if (c1, c3) not in (('M', 'S'), ('S', 'M')):
			continue
		if c1 == c2 and c3 == c4 and data[y + 1][x + 1] == 'A':
			return 1
	return 0  # Ensure this is outside the loop to always return an integer



silver = 0
gold = 0

for y, row in enumerate(data):
	for x, ch in enumerate(row):
		silver += is_match(data, y, x)
		gold += is_x_mas(data, y, x)
print(silver, gold)
