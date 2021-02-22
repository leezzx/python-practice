# 10-1 예외처리 : 에러가 발생했을 때 그에 대한 처리
try: # try내에 ValueError나 ZeroDivisionError가 있을 경우 해당except항목을 실행
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요.")) # 첫 번째 숫자를 입력하세요.숫자입력
    num2 = int(input("두 번째 숫자를 입력하세요.")) # 두 번째 숫자를 입력하세요.숫자입력
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.") # 숫자를 안넣고 문자를 넣을 경우 = 에러! 잘못된 값을 입력하였습니다.
except ZeroDivisionError as err:
    print(err) # 0으로 나눌 경우 / print(err) : 해당하는 에러 내용 그대로 출력 = division by zero

try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요."))) # 첫 번째 숫자를 입력하세요.숫자입력
    nums.append(int(input("두 번째 숫자를 입력하세요."))) # 두 번째 숫자를 입력하세요.숫자입력
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # ValueError, ZeroDivisionError외 나머지 모든 에러 처리 / Exception as err : 모든 에러에 대해 그 원인 찾기
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) # nums.append(int(nums[0] / nums[1]))줄이 없을 경우 = list index out of range



# 10-2 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: # 두 자리 이상 숫자 입력할 경우
        raise ValueError # ValueError 발생시키기
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")



# 10-3 사용자 저의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg # BigNumberError발생 시 메시지 추가
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # BigNumberError 발생시키기
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.") # 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
    print(err) # 입력값 : num1, num2



# 10-4 finally : 오류가 발생하건 말건 무조건 실행되는 구문
finally:
    print("계산기를 이용해 주셔서 감사합니다.") # 정의된, 정의안된 어떠한 오류의 경우라도 실행 = 계산기를 이용해 주셔서 감사합니다.



# 10-5 Quiz
'''동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력허였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

[코드]
chicken = 10
waiting = 1 # 홀 안에는 만석, 대기번호 1부터 시작
while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1
        chicken -= order'''

chicken = 10
waiting = 1 # 홀 안에는 만석, 대기번호 1부터 시작
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1 or order > 10:
            raise ValueError
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break