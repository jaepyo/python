#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    #여기에 코드를 작성해주세요.
    count = 0

    h = len(height)
    w = len(height[0])
    
    for i in range(h):
        for j in range(w):
            is_danger = True
            if 0 <= i-1 < h and height[i][j] >= height[i-1][j]:
                is_danger = False
            if 0 <= i+1 < h and height[i][j] >= height[i+1][j]:
                is_danger = False
            if 0 <= j-1 < w and height[i][j] >= height[i][j-1]:
                is_danger = False
            if 0 <= j+1 < w and height[i][j] >= height[i][j+1]:
                is_danger = False
            if is_danger:
                count += 1
 
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
