n = int(input())
if n %1000 == 0:
    print(0)
    exit()
print(1000 - (n % 1000))