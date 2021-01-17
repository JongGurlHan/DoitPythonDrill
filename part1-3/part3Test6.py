#리스트 중에서 홀수에만 2를 곱하여 저장
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]

# for num in numbers:
#     if num % 2 == 1 : 
#         result.append(num*2)
print(result)

