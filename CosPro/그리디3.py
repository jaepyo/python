##################
# 모험가 길드(내답)
##################

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 ㅜㅅ있따.
# 여행을 떠날수있는 모임 최댓값
#  2 3 1 2 2 인 경우 그룹 

n = int(input("모험가의 수를 입력하세요 : "))

# xlist = [int(sys.stdin.readline()) for i in range(n)]

xlist = list(map(int, input("공포도를 입력하세요 : ").split()))
xlist.sort()

result  = 0 # 총 그룹의 수
count = 0 #  현재 그룹에 포함된 모험가의 수

for i in xlist: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력