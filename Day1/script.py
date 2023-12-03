import re

fs = open('input.txt').read()

def sumOfCalibratedValues(text):
    reg = 'one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9'

    def calcSumPerLine(line):
        # Create map of words and digits
        numMap = {n: str(i % 9 + 1) for i, n in enumerate(reg.split('|'))}
        
        # Creates list of all number occurances, spelled-out numbers inclusive
        x = [numMap.get(match) for match in re.findall(rf'(?=({reg}))', line)]
        
        return int(x[0] + x[-1])

    return sum(calcSumPerLine(line) for line in text.strip().split('\n'))

# Using the suggested method to calculate the sum of calibration values
print(sumOfCalibratedValues(fs))

