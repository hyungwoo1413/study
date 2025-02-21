"""
02_문제

갑자기 분노한 찬수는 문자열 커팅기에 집착하여 아예 문자열을 산산조각 내버렸습니다.
우리는 찬수가 조각내버린 문자열을 가지고 기존의 문자열을 복원해야합니다.

산산조각난 문자열은 리스트에 저장되어있습니다.
조각난_문자열 = ['a','c','d','p','p','l','e']

복원_문자열 = 'apple'

조각난 문자열을 꺼내어 문자열을 복원할 수 있는지 여부가 궁금합니다.
복원이 가능하다면 True
불가능하다면 False 를 리턴해주세요.

r_str : 복원해야할 문자열입니다.
d_str : 조각난 문자열의 모음입니다.
"""
d_str = ['a','q','e','h','l','p','l','c','w','p']
r_str = 'apple'

d_str2 = ['a','q','c','g','a','e','l','c','w','p']
r_str2 = 'graph'

d_str3 = ['c','c','c','a','b','e','c']
r_str3 = 'ace'
def solution(r_str, d_str):
    return


print(solution(r_str,d_str))        # True
print(solution(r_str2,d_str2))      # False
print(solution(r_str3,d_str3))      # True

