list = []

for i in range(9) :
    i = int(input())
    list.append(i)
    
print(max(list))
print(list.index(max(list)) + 1)