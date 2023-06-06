a = int(input())
b = int(input())
print(a*(b%10))

print(a*((b//10)%10))  
print(a*((b%100)//10)) # 위와 같은 답

print(a*(b//100))
print(a*b)