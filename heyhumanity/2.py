def f(x,y,z,w):
    return ((x <= w) or y and (not z)) and ((y <= (not z)) or x and (not w))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x,y,z,w):
                    print(x,y,z,w)