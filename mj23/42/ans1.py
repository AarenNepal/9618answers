global Animals #array of string
Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

def SortDescending():
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength):
        for y in range(0, ArrayLength-x-1):
            if Animals[y][0:1] < Animals[y+1][0:1]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp

SortDescending()
for each in Animals:
    print(each)