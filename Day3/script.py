import math, re

fs = open('input.txt').read().split('\n')

# get dict of indices that are symbols, empty list to be populated w/ part numbers
#  i forgor the 0 in the string...
indicesDict = {(row, col): [] for row in range(len(fs)) for col in range(len(fs[0])) if fs[row][col] not in '0987654321.'}


for r, row in enumerate(fs):
    for n in re.finditer(r'\d+', row):
        indicesDict.update({ind: indicesDict[ind] + [int(n.group())] for ind in 
                        {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}
                        if ind in indicesDict})
            




# with open('out.txt', "w") as f:
#     print(indicesDict, file=f)


a = sum(sum(x) for x in indicesDict.values())
b = sum(math.prod(x) for x in indicesDict.values() if len(x) == 2)
print(a, b)
