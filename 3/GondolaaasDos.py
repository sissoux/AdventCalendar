import re

def getStartEnd(string:str)->list:
    out = list()
    for match in re.finditer(r'\d+', string):
        out.append({"value":int(match.group()), "start":match.start(), "end":match.end()})
    return out

inputLines = open("input.txt", "r").readlines()
inputNumberList = [getStartEnd(line) for line in inputLines]

sum = 0

for y, line in enumerate(inputLines):
    line = line.rstrip()
    for x, char in enumerate(line):
        if char == "*":
            proxiNumber = []
            for l in range(y-1, y+2):
                try:
                    for number in inputNumberList[l]:
                        if not(number["end"] < x or number["start"]>=x+2):
                            proxiNumber.append(number)
                except IndexError:
                    pass
            print(f"{proxiNumber=} in {x=}, {y=}")
            if len(proxiNumber)==2:
                sum += int(proxiNumber[0]["value"])*int(proxiNumber[1]["value"])
                print(f"Gear found in {x=} {y=}")

print(sum)