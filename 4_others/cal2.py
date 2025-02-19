# class_basic_exam 을 통과하지 못한자, 얼른 이 창을 닫으세요.

# 상속

# 형우는 옛날에 계산기를 만들다가 빠르게 때려치웠다.
# 그 유산인 calc_ver01 클래스를 발견하고, 계산기의 남은 기능들을 구현해보려고한다.
class calc_ver01():
    def __init__(self):
        self.accum = 0

    def __str__(self):
        return f'{self.accum}'

    def add(self,a):
        self.log.append(self.accum)
        self.stack.clear()
        self.accum += a
        return print(self.accum)
    
# 클래스명(클래스명) 으로 상속받을 수 있다.
class calc_ver02(calc_ver01):
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자를 실행한다. 즉 calc_ver01 의 init 을 실행한다
                            # 생성자를 호출하는 이유 : 부모클래스의 멤버변수를 사용하려고, 호출하지않아도 메서드(함수)는 사용이 가능하다.
    def sub(self,a):
        self.log.append(self.accum)
        self.stack.clear()
        self.accum -= a
        return print(self.accum)


class calc_ver03(calc_ver02):
    def __init__(self, num):
        super().__init__()
        self.accum = num
        self.log = []
        self.stack = []
    
    def _record(self):
        self.log.append(self.accum)
        self.stack.clear()

    def mul(self, a):
        self.log.append(self.accum)
        self.stack.clear()
        self.accum *= a
        return print(self.accum)

    def div(self, a):
        if a != 0:
            self._record()
            self.accum /= a
        else:
            print("0으로 나눌 수 없습니다!")
    
    def undo(self):
        if not self.log:
            print('undo 할 기록이 없습니다.')
        else:
            self.stack.append(self.accum)
            self.accum = self.log.pop()

    def redo(self):
        if not self.stack:
            print('redo 할 기록이 없습니다.')
        else:
            self.log.append(self.accum)
            self.accum = self.stack.pop()



if __name__ == "__main__":
    new_calc = calc_ver03(5)    # 5
    new_calc.undo()             # 에러 , 예외처리 요망 ('undo 할 기록이 없습니다' 출력)
    new_calc.add(3)             # 8
    new_calc.div(2)             # 4
    new_calc.undo()             # 8
    new_calc.redo()             # 4
    new_calc.redo()             # 에러 , 예외처리 요망 ('redo 할 기록이 없습니다' 출력)

    print(new_calc.log)
    print(new_calc.stack)


    
# 제대로 되었나 확인해보자.

# dongkwan_calc = calc_ver01()
# print(dongkwan_calc.add(3))  # 3
# # calc.sub(3)  : 에러 , why? ver01에는 구현되지 않음

# hyungwoo_calc = calc_ver02()
# print(hyungwoo_calc.add(4))  # 4
# print(hyungwoo_calc.sub(3))  # 1


# ver01을 사용한 동관의 계산기는 sub기능이 동작하지 않지만, 최신버전을 가진 형우의 계산기는 이전버전의 add와 최신버전의 sub 기능 둘다 사용이 가능하다.


# 틈새 지식 주입 , hyungwoo_calc, dongkwan_calc 은 서로 같은 클래스이지만 다른 인스턴스 이기 때문에, self.accum 은 각자 존재한다.


"""
-챌린지-

형우는 곱하기와 나눗셈을 하고싶은 욕심이 생겼습니다.

calc_ver03 버전의 클래스를 만들어 욕심을 채우세요.

규칙.
calc_ver03 은 calc_ver02 를 상속받습니다.

실행되어야 할 동작은 다음과 같습니다.

new_calc = calc_ver03(5)    -> 부모 생성자 호출, 그리고 self.accum = 5 가 동작합니다, 힌트) __init__

new_calc.mul(3) = self.accum * 3
new_calc.div(3) = self.accum / 3

print(new_calc) = 현재 계산된 결과 출력 ex) add(3) sub(2) 를 실행 한 후 프린트를 하면 1이 나옵니다.
tip) __str__ 을 연구하다보면 답이 나올 것이다.


-도전 챌린지-
undo(뒤로가기)와 redo(앞으로가기) 기능을 구현해주세요.

예시)
new_calc = calc_ver03(5)    # 5
new_calc.undo()             # 에러 , 예외처리 요망 ('undo 할 기록이 없습니다' 출력)
new_calc.add(3)             # 8
new_calc.div(2)             # 4
new_calc.undo()             # 8
new_calc.redo()             # 4
new_calc.redo()             # 에러 , 예외처리 요망 ('redo 할 기록이 없습니다' 출력)

tip) 계산 히스토리를 기록할 수 있다면?
제약조건은 없습니다. 기능 구현에 머리를 써주세요.
"""