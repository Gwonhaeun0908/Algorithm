def solution(order):
    menu_prices = {
        "차가운 아메리카노": 4500,
        "따뜻한 아메리카노": 4500,
        "차가운 카페 라테": 5000,
        "따뜻한 카페 라테": 5000,
        "아메리카노": 4500,
        "카페 라테": 5000,
        "아무거나": 4500
    }
    
    answer = 0
    
    for item in order:
        if "americano" in item:
            answer += menu_prices["아메리카노"]
        elif "cafelatte" in item:
            answer += menu_prices["카페 라테"]
        else:
            answer += menu_prices["아무거나"]
            
    return answer