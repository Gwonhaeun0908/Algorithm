def solution(myString):
    string = myString.split("x")
    
    answer = []
    
    for string in string :
        answer.append(len(string))
    
    return answer