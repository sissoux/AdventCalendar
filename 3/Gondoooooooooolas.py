import re

def getStartEnd(string:str)->list:
    out = list()
    for match in re.finditer(r'\d+', string):
        out.append({"value":int(match.group()), "start":match.start(), "end":match.end()})
    return out

inputLines = open("input.txt", "r").readlines()
inputNumberList = [getStartEnd(line) for line in inputLines]

sum = 0

for i, line in enumerate(inputLines):
    line = line.rstrip()
    for number in inputNumberList[i]:
        ValidNumber = False
        for x in range(max(0,number["start"]-1), min(number["end"]+1,len(line))):
            if ValidNumber : 
                break
            for y in range(i-1, i+2):
                if y >= 0 and y < len(inputLines):
                    c = inputLines[y][x]
                    if not c.isnumeric() and not c == '.':
                        ValidNumber = True
                        break
        sum += ValidNumber * number["value"]
print(sum)