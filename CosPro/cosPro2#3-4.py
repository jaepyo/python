#다음과 같이 import를 사용할 수 있습니다.
#import math

# zip함수 : 여러 개의 순회가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를
# 튜플 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다. 
# 이거 잘 활요하면 미쳤따'


def solution(words, word):
    #여기에 코드를 작성해주세요.
    count = 0

    for comp in words:
        for x, y in zip(comp, word):
            if x != y:
                count = count + 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
