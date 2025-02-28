import bingo
import rockscc
### CLI 

"""
기능 부터 만들어도되고
UI부터 만들어도 됩니다.

CLI UI가 별거없음.
"""


while True:
    print('강황석준 조의 미니게임 천국에 오신걸 환영합니다!')
    print('메뉴선택')
    print('1: 가위바위보게임 | 2: 빙고게임 | 3: 프로그램 종료')

    command = int(input())

    if command == 1 : 
        rockscc.GawiBawiBo()
        pass
    elif command == 2 :
        bingo.bingo()       # import 된 bingo.py 안의 bingo 함수를 실행한다.
        pass
    elif command == 3 : # 종료
        print('프로그램을 종료합니다.')
        break

