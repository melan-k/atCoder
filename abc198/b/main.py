s = input()
for i in range(10):
    print(s[::-1])
    if s == s[::-1]:
        print('Yes')
        exit()
    s = s + '0'
print('No')