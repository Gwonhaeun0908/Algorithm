nums = []

for i in range(10) :
    n = int(input())
    nums.append(n % 42)

nums = set(nums)
print(len(nums))