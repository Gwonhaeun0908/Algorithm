n = int(input())
scores = list(map(int, input().split()))
max = max(scores)

result = []
for i in scores : 
   result.append(i / max * 100)
   
print(sum(result) / n)