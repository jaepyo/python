# def solution(s):
#     answer = s
#     num_s = { 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9};
    
#     for item in num_s.items():
#         answer = answer.replace(item[0], str(item[1]))
#     return int(answer)

# #아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# s1 = "one4seveneight"
# ret1 = solution(s1)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret1, "입니다.")

# s2 = "23four5six7"
# ret2 = solution(s2)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret2, "입니다.")

# s3 = "2three45sixseven"
# ret3 = solution(s3)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret3, "입니다.")

# s4 = "123"
# ret4 = solution(s4)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret4, "입니다.")

# answer = "2three45sixseven"
# num_s = { 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9};
# # for item in num_s.items():
# #         answer = answer.replace(item[0], str(item[1]))
# # print(answer)

# for item in num_s.items():
#     print(item)

# answer = "2three45sixseven"
# for i in answer:
#     print(i)

