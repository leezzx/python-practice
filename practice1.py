# 2-1 숫자 자료형
print(5) 
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1)) 



# 2-2 문자열 자료형
print('풍선') 
print("나비")
print("ㅋ"*9)



# 2-3 boolean 자료형 - 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))



# 2-4 변수 - 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
name = "흰둥이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")로도 표현 가능(','는 'str'없이 사용 가능)
print(name + "는 어른일까요? " + str(is_adult))



# 2-5 주석
''' 세개를 사용하여
여러문장을
주석처리 할 수 있다'''
# 필요한 문장 드래그 후 'Ctrl+/'를 하여 한번에 가능



# 2-6 Quiz
'''변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력문장 : XX행 열차가 들어오고 있습니다.'''

station = '사당'
print(station + "행 열차가 들어오고 있습니다.")
station = '신도림'
print(station + "행 열차가 들어오고 있습니다.")
statiom = '인천공항'
print(station + "행 열차가 들어오고 있습니다.")