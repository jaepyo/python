# 시각
# 완전 탐색(Brute Forcing)

# h = int(input('시간을 입력해주세요 : '))

# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
# print(count)

h = int(input('시간을 입력해주세요 : '))

count = 0

for i in range(0,h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                 count += 1

print(count)