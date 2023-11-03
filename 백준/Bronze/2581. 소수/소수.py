m=int(input())
n=int(input())
    
nums = []

for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            nums.append(i)

if len(nums)<1:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
