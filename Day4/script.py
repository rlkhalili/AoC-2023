fs = open("input.txt").readlines()

cards = [1 for _ in fs] 
score = 0
for i, l in enumerate(fs):
    x, y = map(str.split, l.split('|'))
    winningNo = len(set(x) & set(y))
    score += 2 ** (winningNo - 1) if winningNo else 0
    for j in range(winningNo):
        cards[i + 1 + j] += cards[i]


print(score, sum(cards))