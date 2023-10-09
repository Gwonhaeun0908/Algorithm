def solution(rank, attendance):
    answer = 0
    top3 = 0
    
    for i in range(1, len(rank) + 1):
        num = rank.index(i)
        
        if attendance[num]:
            answer += num * 100 ** (2 - top3)
            top3 += 1
        
        if top3 == 3:
            break
            
    return answer