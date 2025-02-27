import random
<<<<<<< HEAD
=======
import time
>>>>>>> 86d37d2c2c8701b9c35925c9fb1face6c22fc073

## 빙고게임 만들어보기.

def bingo():
## --------------------
    bingoBoard = [[0 for _ in range(4)] for _ in range(4)] # 4 x 4 생성
    memo = []
    bingoState = {}
    score = 0
## --------------------

    ## bingoBoard = 랜덤한 숫자를 넣는 로직
    for row in range(len(bingoBoard)) : # 실제 행을 나타냄.
        for col in range(len(bingoBoard)) : # 실제 열을 나타냄.
            while True:
                bingoBoard[row][col] = random.randint(1,51)
                if bingoBoard[row][col] in memo:
                    continue
                else:
                    memo.append(bingoBoard[row][col])
                    break

    for row in bingoBoard:          # [[],[],[]] => row = []
        for col in row:             # [0,0,001] => 0?
            bingoState[col] = False # {3 : False,}

    while True:
        print('Your turn : ')
        playerPick = int(input('숫자 선택 : '))
        # 빙고보드안에 있는 숫자인지 판단
        if playerPick in memo:
            bingoState[playerPick] = True
            print(f'{playerPick} 색칠 완료')
        else:
            print('빙고보드에 없는 숫자임 ㅋ')
        
        for i in bingoBoard:
            for j in i:
                if bingoState[j] == True:
                    print('O', end=' ')
                else : print('X', end=' ')
            print()
            print()

        ## 스코어 어떻게 체크하지? , 로직 개선해야됨 
        ## 1. 탐색 , 2. 스코어 올라가는 로직
        # 가로 
<<<<<<< HEAD
        
=======
>>>>>>> 86d37d2c2c8701b9c35925c9fb1face6c22fc073
        if bingoState[memo[0]] and bingoState[memo[1]] and bingoState[memo[2]] and bingoState[memo[3]]:
            score += 1
        if bingoState[memo[4]] and bingoState[memo[5]] and bingoState[memo[6]] and bingoState[memo[7]]:
            score += 1
        if bingoState[memo[8]] and bingoState[memo[9]] and bingoState[memo[10]] and bingoState[memo[11]]:
            score += 1
        if bingoState[memo[12]] and bingoState[memo[13]] and bingoState[memo[14]] and bingoState[memo[15]]:
            score += 1
        
        # 세로
        if bingoState[memo[0]] and bingoState[memo[4]] and bingoState[memo[8]] and bingoState[memo[12]]:
            score += 1
        if bingoState[memo[1]] and bingoState[memo[5]] and bingoState[memo[9]] and bingoState[memo[13]]:
            score += 1
        if bingoState[memo[2]] and bingoState[memo[6]] and bingoState[memo[10]] and bingoState[memo[14]]:
            score += 1
        if bingoState[memo[3]] and bingoState[memo[7]] and bingoState[memo[11]] and bingoState[memo[15]]:
            score += 1

        # 대각선
        if bingoState[memo[0]] and bingoState[memo[5]] and bingoState[memo[10]] and bingoState[memo[15]]:
            score += 1
<<<<<<< HEAD
        if bingoState[memo[12]] and bingoState[memo[9]] and bingoState[memo[6]] and bingoState[memo[3]]:
            score += 1
            
=======
        if bingoState[memo[3]] and bingoState[memo[6]] and bingoState[memo[9]] and bingoState[memo[12]]:
            score += 1
>>>>>>> 86d37d2c2c8701b9c35925c9fb1face6c22fc073

        if score == 3:
            print('게임 클리어!')
            break
        
        
        



