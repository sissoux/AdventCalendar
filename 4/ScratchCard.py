total  = 0
for line in open("4/input.txt", "r").readlines():
    game = line.strip().split(":")[1].split("|")
    winning=[int(x) for x in game[0].split()]
    draw=[int(x) for x in game[1].split()]
    points = sum([x in winning for x in draw])
    total += (2**(points-1))*(points!=0)
    
print(int(total))