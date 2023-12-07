
games = open("4/input.txt", "r").readlines()
totalCards = [1 for x in games]
for i, line in enumerate(games):
    game = line.strip().split(":")[1].split("|")
    winning=[int(x) for x in game[0].split()]
    draw=[int(x) for x in game[1].split()]
    points = sum([x in winning for x in draw])
    for x in range(points):
        totalCards[i+x+1] +=1*totalCards[i]

result = sum([x for x in totalCards])
print(result)