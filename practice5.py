# 6-1 if
weather = "비"
'''if 조건 :
       실행 명령문'''
if weather == "비":
    print("우산을 챙기세요.") # weather = "맑음"일 경우 아무것도 출력 안됨

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요없어요.") # 마스크를 챙기세요.

weather = input("오늘 날씨는 어때요? ") # 입력값에 따라 결과가 달라짐
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요없어요.") # 오늘 날씨는 어때요? '비'라고 입력 -> 우산을 챙기세요.

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")



# 6-2 for (반복문)
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 0 ~ 4
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 0 ~ 4
for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 1 ~ 5

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer)) 
    '''아이언맨, 커피가 준비되었습니다.
       토르, 커피가 준비되었습니다.
       그루트, 커피가 준비되었습니다.'''



# 6-3 while (반복문)
customer = "토르"
index = 5
while index >= 1: # 조건을 만족할 때까지 반복
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")
        '''토르님, 커피가 준비 되었습니다. 5번 남았어요.
           토르님, 커피가 준비 되었습니다. 4번 남았어요.
           토르님, 커피가 준비 되었습니다. 3번 남았어요.
           토르님, 커피가 준비 되었습니다. 2번 남았어요.
           토르님, 커피가 준비 되었습니다. 1번 남았어요.
           커피가 폐기처분되었습니다.'''        

'''customer = "아이언맨"
   index = 1
   while True:
       print("{0}님, 커피가 준비 되었습니다. 호출 {1}회".format(custpmer, index))
       index += 1 # 무한루프로 호출이 올라감. Ctrl + C로 빠져나갈 수 있음'''

customer = "토르"
person = "Unknown"

while person != customer: # '토르'가 올 때까지 반복
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    '''토르님, 커피가 준비 되었습니다.
       이름이 어떻게 되세요? 아이언맨
       토르님, 커피가 준비 되었습니다.
       이름이 어떻게 되세요? 구르트
       토르님, 커피가 준비 되었습니다.
       이름이 어떻게 되세요? 토르'''



# 6-4 continue와 break (반복문 내에서 활용)
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue # 반복문 계속 진행
    elif student in no_book:
        print("오늘 수업 여기까지, {0}은 교무실로 따라와.".format(student))
        break # 반복문 탈출
    print("{0}야 책을 읽어봐.".format(student))
    '''1야 책을 읽어봐.
       3야 책을 읽어봐.
       4야 책을 읽어봐.
       6야 책을 읽어봐.
       오늘 수업 여기까지, 7은 교무실로 따라와.'''



# 6-5 한 줄 for
# 출석번호 1, 2, 3, 4를 101, 102, 103, 104로 바꾸는 경우
students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

# 학생이름을 길이로 변환
students = ["iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

# 학생이름을 대문자로 변환
students = ["iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']



# 6-6 Quiz
'''당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1. 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정한다.
조건2. 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분'''

from random import *
cnt = 0
for coco in range(1, 51):
    time = randrange(5, 51)
    if time <= 15 and time >= 5:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(coco, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(coco, time))

print("총 탑승 승객 : {0}분".format(cnt))