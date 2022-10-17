# 그리디 알고리즘

# 거스름 돈 문제

# # 거슬러 줘야할 돈 n
# n = 1260
# count = 0

# # 큰 단위의 화폐부터 차례대로 확인하기
# array = [500, 100, 50, 10]

# for coin in array:
#     count += n //coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)

##################
# 1이 될 때까지 (내답)
##################
n = int(input('첫번째 수를 입력하세요 : '))
k = int(input('두번째 수를 입력하세요 : '))
count = 0

while n > 1:
    if n%k == 0:
        n = n//k
        count += 1
    else:
        n = n-1
        count += 1

print(count)


##################
# 1이 될 때까지 (정답)
##################

# # n,k를 공백을 기준으로 구분하여 입력받기
# n, k = map(int, input().split())

# result  = 0
# while True:
#     # n이 k로 나누어 떨어지는 수가 될때까지 빼기
#     target = (n//k) * k
#     result += (n-target)
#     n = target
#     # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#     if(n<k):
#         break
#     # k로 나누기
#     result += 1
#     n//=k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)

