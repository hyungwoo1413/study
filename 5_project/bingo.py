import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_bingo_board(size=4, num_range=50):
    numbers = random.sample(range(1, num_range + 1), size * size)  # 중복 없는 숫자 생성
    return [numbers[i * size:(i + 1) * size] for i in range(size)]

def check_bingo(bingo_state):
    size = len(bingo_state)
    bingo_count = 0

    # 가로 체크
    for row in bingo_state:
        if all(row):
            bingo_count += 1

    # 세로 체크
    for col in range(size):
        if all(bingo_state[row][col] for row in range(size)):
            bingo_count += 1

    # 대각선 체크
    if all(bingo_state[i][i] for i in range(size)):  # 좌상 → 우하
        bingo_count += 1
    if all(bingo_state[i][size - 1 - i] for i in range(size)):  # 우상 → 좌하
        bingo_count += 1

    return bingo_count

def print_board(bingo_board, bingo_state):
    size = len(bingo_board)
    print("\n=== Bingo Board ===")
    for i in range(size):
        for j in range(size):
            print(' O ' if bingo_state[i][j] else bingo_board[i][j], end=' ')
        print("\n")
    print("===================")

def bingo():
    size = int(input('빙고보드판 사이즈를 입력해주세요 : [3 ~ 9] 사이 숫자입력 : '))
    bingo_board = generate_bingo_board(size)
    bingo_state = [[False] * size for _ in range(size)]  # 숫자 선택 여부

    while True:
        clear_terminal()
        print_board(bingo_board, bingo_state)

        # 👉 숫자 입력 받기
        try:
            player_pick = int(input(f"숫자 선택 [1 ~ 50]: "))
        except ValueError:
            print("⚠️ 숫자를 입력하세요!")
            input("계속하려면 Enter 입력...")
            continue

        # 선택한 숫자 찾기 및 표시
        found = False
        for i in range(size):
            for j in range(size):
                if bingo_board[i][j] == player_pick:
                    bingo_state[i][j] = True
                    found = True
                    print(f"✅ {player_pick} 선택 완료!")
                    break

        if not found:
            print("❌ 빙고 보드에 없는 숫자입니다!")

        # 빙고 체크 및 결과 출력
        score = check_bingo(bingo_state)
        print(f"현재 빙고 개수: {score}")
        
        if score >= 3:
            print("\n🎉 게임 클리어! 🎉")
            break

        input("\n계속하려면 Enter 입력...")
