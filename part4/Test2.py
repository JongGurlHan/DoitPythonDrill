# 입력으로 들어온 모든 수의 평균 값을 계산해주는 함수를 작성해보자
# (단 입력으로 들엉오는 수의 개수는 정해져 있지 않다.)

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)    

print(avg_numbers(1,2,3,4,5))
    

