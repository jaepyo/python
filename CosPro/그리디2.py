##################
# 곱하기 혹은 더하기(내답)
##################

num_list = list(map(int, input().split()))
t1 = 0
t2 = 0
t3 = int(num_list[0])

for i in range(0,len(num_list)-1):
    t1 = t3 + num_list[i+1]
    t2 = t3 * num_list[i+1]
    if t1 > t2:
        t3 = t1 
    else:
        t3 = t2

print(t3) 

##################
# 곱하기 혹은 더하기(정답)
##################

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)