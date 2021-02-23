import itertools
x = int(input())
if x < 100:
    print(0)
    exit()
if x >= 2000:
    print(1)
    exit()

for combination in itertools.combinations_with_replacement(range(20), 6):
    price = combination[0]*100 + combination[1]*101 + combination[2]*102 + combination[3]*103 + combination[4]*104 + combination[5]*105
    if x == price:
        print(1)
        exit()
print(0)