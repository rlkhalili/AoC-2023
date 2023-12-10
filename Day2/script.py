import re

gameData = open('input.txt').read().split('\n')    # line-by-line

def calcTotalPower(gamesData):
    totalPow = 0

    for game in gamesData:
        # find every occurrence of the no. of cubes per color and get the max
        maxRed = max(map(int, re.findall(r'(\d+) red', game))) if 'red' in game else 1
        maxGreen = max(map(int, re.findall(r'(\d+) green', game))) if 'green' in game else 1
        maxBlue = max(map(int, re.findall(r'(\d+) blue', game))) if 'blue' in game else 1

        power = maxRed * maxGreen * maxBlue
        totalPow += power

    return totalPow


print(calcTotalPower(gameData))