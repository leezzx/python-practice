# 4-1 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)



# 4-2 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # jumin 중 7번째 자리의 값 가져오기 = 1
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지의 값 가져오기 = 99
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 21
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지의 값 가져오기 = 990120
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지의 값 가져오기 = 1234567
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 = 1234567



# 4-3 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자가 소문자
print(python.upper()) # 모든 문자가 대문자
print(python[0].isupper()) # 0번째 값이 대문자가 맞는지 = True
print(len(python)) # 전체 문자열의 길이 반환 = 17
print(python.replace("Python", "Java")) # 문자열의 특정 단어를 바꿔줄 때 = Java is Amazing

index = python.index("n")
print(index) # 문자열에서 n이라는 값이 몇번째에 위치하는지 = 5
index = python.index("n", index + 1) # 문자열에서 n을 찾은 이후 값 부터 다음 n값 찾기 = 15
print(index)

print(python.find("n")) # 5
print(python.find("Java")) # -1 : 프로그램은 계속 진행됨
print(python.index("Java")) # 오류 : 바로 프로그램이 종료됨

print(python.count("n")) # 문자열에서 n이 총 몇번 등장하는지 = 2



# 4-4 문자열 포맷
print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20) # 나는 20살 입니다.(d는 항상 정수 값만 가능)
print("나는 %s을 좋아해요." % "파이썬") # 나는 파이썬을 좋아해요.(s는 정수, 문자열 값 가능)
print("Apple 은 %c로 시작해요." % "A") # Apple 은 A로 시작해요.(c는 한 글자만 가능)
print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.

print("나는 {}살입니다." .format(20)) #나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요." .format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요." .format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요." .format("파랑", "빨강")) # 나는 빨강색과 파랑색을 좋아해요.

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨강")) # 나는 20살이며, 빨강색을 좋아해요.
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨강", age = 20)) # 나는 20살이며, 빨강색을 좋아해요.

age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 나는 20살이며, 빨강색을 좋아해요.



# 4-5 탈출 문자
print("백문이 불여일\n백견이 불여일타") # \n : 줄바꿈

print('저는 "나도코딩"입니다.') # 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.") # 저는 '나도코딩'입니다.
print("저는 \"나도코딩\"입니다.") # \",\' : 문장 내에서 따옴표 = 저는 "나도코딩"입니다.
print("저는 \'나도코딩\"입니다.") # 저는 '나도코딩'입니다.

print("C:\\Users\\Leessx\\Desktop\\PythonWorkspace>") # \\ : 문장 내에서 \ = C:\Users\Leessx\Desktop\PythonWorkspace>

print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동 = PineApple

print("Redd\bApple") # \b : 백스페이스(한 글자 삭제) = RedApple

print("Red\tApple") # \t : 탭 = Red   Apple



# 4-6 Quiz
'''사이트별로 비밀번호를 만들어 주는 프로그램을 작성해보시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e'개수(1) + '!'로 구성
생성된 비밀번호  : nav51!'''

url = "http://naver.com"
my_str = url.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2 = my_str[0.5]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙3
print("{0}의 비밀번호는 {1}입니다.".format(url, password))