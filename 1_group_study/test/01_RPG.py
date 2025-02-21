"""
01_ 문제

RPG 게임의 용사가 있습니다.
attack 리스트에는 피격 된 정보가 저장되어 있습니다.
-1 : 회피
0 : 골렘
1 : 리본돼지
2 : 슬라임

monsters 딕셔너리에는 몬스터별 공격력이 저장되어 있습니다.

attack 을 입력 받았을 때, 모든 공격이 끝난 후 용사의 hp를 리턴해주세요.

예외 : hp가 0이 되면 남은 공격이 있든 없든, 사망합니다. 캐릭터가 사망했다면, -1을 리턴해주세요.
"""

# 테스트 케이스 1
hp = 200
monsters = {'골렘' : 40 , '리본돼지' : 20 ,'슬라임' : 10}


# 테스트 케이스
attack = [-1,0,1,1,0,2,-1,1]        
attack2 = [0,0,0,0,0,2,-1,1]        
attack3 = [-1,-1,1,1,0,2,-1,1]      
attack4 = [-1,-1,-1,-1,-1,-1,-1,-1] 


def solution(hp,monsters,attack):
    
    return hp


print(solution(hp,monsters,attack))     # 50
print(solution(hp,monsters,attack2))    # -1
print(solution(hp,monsters,attack3))    # 90
print(solution(hp,monsters,attack4))    # 200