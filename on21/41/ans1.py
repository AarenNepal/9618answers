def Unknown(X, Y):
    if X < Y:
        print(X+Y)
        return Unknown(X+1, Y)*2
    elif X == Y:
        return 1
    else:
        print(X+Y)
        return Unknown(X-1, Y) // 2

def IterativeUnkown(X, Y):
    Total = 1
    while X != Y:
        print(str(X + Y))
        if X < Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X - 1
            Total = int(Total / 2)
    return Total

#main
print("X= 10, Y=15")
print(str(Unknown(10, 15)))

print("X= 10, Y=10")
print(str(Unknown(10, 10)))

print("X= 15, Y=10")
print(str(Unknown(15, 10)))

print("X= 10, Y=15")
print(str(IterativeUnkown(10, 15)))

print("X= 10, Y=10")
print(str(IterativeUnkown(10, 10)))

print("X= 15, Y=10")
print(str(IterativeUnkown(15, 10)))

