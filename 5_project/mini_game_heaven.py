import os
import keyboard
import bingo
import time
### CLI 

"""
기능 부터 만들어도되고
UI부터 만들어도 됩니다.

CLI UI가 별거없음.
"""
def clearScreen(): # os에 특화된 팁
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def check(num, select):
    point = '<--'
    if num == select:
        return point
    return ''

def main():
    num = 1
    while True:
        clearScreen()
        print('강황석준 조의 미니게임 천국에 오신걸 환영합니다!')
        print()
        print('메뉴선택')
        print(f'1: 가위바위보게임 {check(1, num)}')
        print(f'2: 빙고게임 {check(2, num)}')
        print(f'3: 프로그램 종료 {check(3, num)}')
        time.sleep(0.1)
        
        if keyboard.is_pressed('down'): 
            if num < 3:
                num += 1
            time.sleep(0.1)
        elif keyboard.is_pressed('up'):
            if num > 1:
                num -= 1
            time.sleep(0.1)
        if keyboard.is_pressed('enter'):
            if num == 1 : 
                print('가위바위보')
                time.sleep(1)
            elif num == 2 :
                bingo.bingo()
            elif num == 3 :
                print('프로그램을 종료합니다.')
                break

if __name__ == "__main__":
    main()