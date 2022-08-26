def solution(classes, m):
    answer = 0
    for students in classes:
        answer += students // m
        if students % m != 0:
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)
