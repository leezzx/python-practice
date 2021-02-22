# 5-1 리스트 []

# 지하철 칸별로 10명, 20명 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가
print(subway.index("조세호")) # 1 (0부터 시작)

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # 맨 뒤에 붙음 = ["유재석", "조세호", "박명수", "하하"]

# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈") 
print(subway) # ["유재석", "정형돈", "조세호", "박명수", "하하"]

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway) # ["유재석", "정형돈", "조세호", "박명수"]

print(subway.pop())
print(subway) # ["유재석", "정형돈", "조세호"]

print(subway.pop())
print(subway) # ["유재석", "정형돈"]

# 같은 이름의 사람이 몇명인지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() # 순서대로 정렬
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집어서 정렬
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]



# 5-2 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # 유재석
# print(cabinet[5])는 프로그래밍 종료
print(cabinet.get(5)) # 오류여도 프로그래밍이 종료 되지 않고 계속됨 = None
print(cabinet.get(5, "사용가능")) # 사용가능

# 사전 값이 존재하는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# 문자열로도 Key 지정 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 페점
cabinet.clear()
print(cabinet) # {}



# 5-3 튜플 : 값을 추가하거나 변경하는 것이 불가능, 사전보다 빠름, 순서존재
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선가스") = 오류

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩") 
print(name, age, hobby) # 김종국 20 코딩



# 5-4 세트 (set) : 집합, 중복안된, 순서없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

# 교집함 (java와 python을 모두 할 수 있는 개발자)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'김태호', '유재석', '박명수', '양세형'}
print(java.union(python)) # {'김태호', '유재석', '박명수', '양세형'}

#차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# python 할 줄 하는 사람이 늘어남
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}

# java를 잊었어요
java.remove("김태호")
print(java) # {'유재석', '양세형'}



# 5-5 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>



# 5-6 Quiz
'''당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성했고 아이디는 1 ~ 20 이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자  : [2, 3, 4]
-- 축하합니다--

(활용예제)
from random import *
1st = [1,2,3,4,5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))'''

from random import * 
party = range(1,21) # 1부터 20까지 숫자를 생성
party = list(party)
shuffle(party)
winners = sample(party, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다--")