InputCombination = {"red":12, "green":13, "blue":14}
IDSum = 0
for l in  open("input.txt", "r").readlines():
    try:
        line = l.replace('\n', '').split(":")
        lineID = int(line[0][5:])
        draws = [x.split(",") for x in line[1].split(";")]
        for draw in draws:
            dat = [x.split(" ")[1:] for x in draw]
            for color in dat:
                if InputCombination[color[1]] < int(color[0]):
                    raise ValueError
        IDSum += lineID
    except ValueError:
        pass

print(f"Valid games ID sum is: {IDSum}")

powerSum = 0    
for l in  open("input.txt", "r").readlines():
    gameDict = {"red":0, "green":0, "blue":0}
    line = l.replace('\n', '').split(":")
    lineID = int(line[0][5:])
    draws = [x.split(",") for x in line[1].split(";")]
    for draw in draws:
        dat = [x.split(" ")[1:] for x in draw]
        for color in dat:
            gameDict[color[1]] = max(gameDict[color[1]], int(color[0]))
    gamepower = 1
    for color in gameDict:
        gamepower *= gameDict[color]
    powerSum += gamepower

print(f"Power sum is: {powerSum}")