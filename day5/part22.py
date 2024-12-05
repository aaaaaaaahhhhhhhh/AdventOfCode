silver = 0
gold = 0
rules = [list(map(int, x.split("|"))) for x in data.strip().splitlines() if x.count("|") == 1]
lines = [list(map(int, x.split(","))) for x in data.strip().splitlines() if x.count(",") != 0]
adj = defaultdict(set)
for a, b in rules:
    adj[a].add(b)
def fuckyou(you):
    fuck = you.copy()
    for f in range(len(fuck)):
        for u in range(f):
            if fuck[u] in adj[fuck[u+1]]:
                fuck[u], fuck[u+1] = fuck[u+1], fuck[u]
    return fuck
for you in lines:
    fuck = fuckyou(you)
    if fuck == you:
        silver += fuck[len(fuck) // 2]
    else:
        gold += fuck[len(fuck) // 2]
print(silver, gold)
