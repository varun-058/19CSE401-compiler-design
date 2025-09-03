def leftrecursion(l):
    final = []
    for i in l:
        temp1 = i.split(" -> ")
        temp2 = temp1[1].split(" | ")
        for j in temp2:
            if temp1[0] == j[0]:
                final.append(f"{temp1[0]}' -> {j[1:]}{temp1[0]}'")
            else:
                if (f"{temp1[0]}" in temp1[1]):
                    final.append(f"{temp1[0]} -> {j}{temp1[0]}'")
                else:
                    final.append(f"{temp1[0]} -> {j}")
    
    shorten = []
    index = []
    for x in range(len(final)):
        tmp = final[x]
        if x not in index:
            for y in range(x+1, len(final)):
                if final[x][:2] == final[y][:2]:
                    tmp += " | " + final[y][6:]
                    index.append(y)
            shorten.append(tmp)
    return shorten

n = int(input("Enter number of Grammer: "))
l = []
for i in range(n):
    l.append(input(f"Enter Grammer {i+1}: "))
result = leftrecursion(l)
for grammer in result:
    if grammer[1] == "'":
        print(grammer + " | ε")
    else:
        print(grammer)