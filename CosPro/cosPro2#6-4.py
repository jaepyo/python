#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0

    count = [0,0,0]

    for card in cards:
        if card[0] == 'red':
            count[0] += 1
        elif card[0] == 'black':
            count[1] += 1
        elif card[0] == 'blue':
            count[2] += 1
        answer += int(card[1])

    if count[0] == 3 or count[1] == 3 or count[2] == 3:
        answer = answer*3    # answer *= 3
    elif count[0] == 2 or count[1] == 2 or count[2] == 2:
        answer = answer*2    # answer *= 2

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")