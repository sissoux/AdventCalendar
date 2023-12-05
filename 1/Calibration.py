import re
result = 0

number = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}


for line in open("input.txt", "r").readlines():
    occur = dict()
    for key in number:
        occur[key] = [m.start() for m in re.finditer(key, line)]
    minchar = len(line)
    maxchar = 0
    firstval = 0
    lastval = 0
    for key in number:
        try:
            if occur[key][0] <= minchar: 
                firstval = number[key]
                minchar = occur[key][0]
            if occur[key][-1] >= maxchar: 
                lastval = number[key]
                maxchar = occur[key][-1]
        except IndexError:
            pass

    result += firstval*10+lastval

print(result)