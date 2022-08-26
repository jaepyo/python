# def func_a(arr): # 어떤 숫자가 몇 개있는지 Count하는 함수
#     counter = [0 for _ in range(1001)] # Count in List, 0 값이 index 1000까지 삽입
#     for x in arr:
#         counter[x] += 1 
#     return counter

# #The following is code to output testcase.
# arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]

# print(func_a(arr))

# words = ["CODE", "COED", "CDEO"]
# word = "CODE"

# count = 0

# for comp in words:
#     for x, y in zip(comp, word):
#         print(x, y)

# used_tv = [0] * 25
# print(used_tv)

# for entry in enumerate(['A','B','C']):
#     print(entry)

#
n = 4
bundle = "cacdbdedccbb"


def func_a(bundle, start):
    return bundle[start::2]

a_cards = func_a(bundle, 0)[:n]

print(a_cards)