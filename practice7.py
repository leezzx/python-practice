# 8-1 표준 입출력
print("python", "Java", sep=", ") # python, Java
print("python", "Java", "JavaScript", sep=" vs ") # python vs Java vs JavaScript
print("python", "Java", sep=",", end="?") # end : 맨 끝에 "?"추가, 다음 줄과 한 줄로 연결
print("무엇이 더 재밌을까요?") # python,Java?무엇이 더 재밌을까요?

import sys
print("python", "Java", file=sys.stdout) # 표준출력 = python Java
print("python", "Java", file=sys.stderr) # 표준에러 = python Java

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    '''수학 0
       영어 50
       코딩 100'''
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust : 8의 공간 확보 후 오른쪽에 정렬, rjust : 4의 공간 확보 후 왼쪽에 정렬
    '''수학      :   0
       영어      :  50
       코딩      : 100'''

# 은행 대기 순번표 : 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num)) # 대기번호 : 1 ~ 20
    print("대기번호 : " + str(num).zfill(3)) # zfill : 3개의 공간 확보 후 빈 공간을 0으로 채우기 = 대기번호 : 001 ~ 021

#표준입력
answer = input("아무 값이나 입력하세요 : ") # input : 항상 문자열 형태로 저장함 = 아무 값이나 입력하세요 : ㅈ
print("입력하신 값은 {0}입니다.".format(answer)) # 입력하신 값은 ㅈ입니다.



# 8-2 다양한 출력포맷
print("{0: >10}".format(500)) # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되. 총 10자리 공간을 확보 =        500
print("{0: >+10}".format(500)) # 양수일 때 +로 표시, 음수일 때 -로 표시 =       +500
print("{0: >+10}".format(-500)) # 양수일 때 +로 표시, 음수일 때 -로 표시 =       -500
print("{0:_<+10}".format(500)) # 왼쪽 정렬하고, 빈칸을 _로 채움, 양수음수 표시 = +500______
print("{0:,}".format(10000000000)) # 3자리 마다 콤마를 찍어주기 = 10,000,000,000
print("{0:+,}".format(-10000000000)) # 3자리 마다 콤마를 찍어주기, 양수음수 표시 = -10,000,000,000
print("{0:^<+30,}".format(1000000000000))# 3자리 마다 콤마를 찍어주기, 양수음수 표시, 총 30자리 공간 확보, 빈 자리는 ^로 채움 = +1,000,000,000,000^^^^^^^^^^^^
print("{0:f}".format(5/3)) # 소수점 출력 = 1.666667
print("{0:.2f}".format(5/3)) # 소수점 3째 자리에서 반올림(2째 자리까지 표시) = 1.67



# 8-3 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # encording="utf8" : 한글 오류 방지, "w" : 쓰기용
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # EXPLORER에 score.txt 파일 생성
'''수학 : 0
   영어 : 50'''

score_file = open("score.txt", "a", encoding="utf8") # "a" : 내용추가
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close() # 기존의 score.txt 파일에 추가
'''수학 : 0
   영어 : 50
   과학 : 80
   코딩 : 100'''

score_file = open("score.txt", "r", encoding="utf8") # "r" : 파일 읽어오기
print(score_file.read()) # read() : 모든 내용 읽기
score_file.close() # score.txt 파일 내용을 TERMINAL로 가져오기
'''수학 : 0
   영어 : 50
   과학 : 80
   코딩 : 100'''

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # readline() : 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close() # 자동 줄바꿈, print(score_file.readline(), end="")를 통해 줄 간격 없앨 수 있음
'''수학 : 0

   영어 : 50

   과학 : 80

   코딩 : 100'''

score_file = open("score.txt", "r", encoding="utf8") # 파일이 몇줄 인지 모를 때
while True: # 무한 루프
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
'''수학 : 0

   영어 : 50

   과학 : 80

   코딩 : 100'''

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # readlines() : 모든 줄을 가져와서 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
'''수학 : 0
   영어 : 50
   과학 : 80
   코딩 : 100'''



# 8-4 pickle : 프로그램 상의 데이터를 파일형태로 저장
import pickle
profile_file = open("profile.pickle", "wb") # "b" : 바이너리 타입(pickle을 쓰기 위해선 항상 b)
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
pickle.dump(profile, profile_file) # dump : profile의 정보를 profile.pickle 파일에 저장
profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile.pickle 파일의 정보를 profile에 불러오기
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()



# 8-5 with
import pickle
with open("profile.pickle", "rb") as profile_file: # with : close할 필요 없음
    print(pickle.load(profile_file)) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요") # EXPLORER에 study.txt 파일 생성 = 파이썬을 열심히 공부하고 있어요
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read()) # 파이썬을 열심히 공부하고 있어요



# 8-6 Quiz
'''당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X주차 주간보고 -
부서 : 
이름 : 
업무요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파링명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.'''

for i in range(1, 51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")