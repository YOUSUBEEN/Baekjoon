test = int(input())

for i in range(test):
    R, S = input().split() 
    rs = ''
    for i in S:
        rs += int(R) * i 
    print(rs)