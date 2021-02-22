# 11-1 모듈 : 함수나 클래스 등의 파이썬 문장들을 담고있는 파일 (.py)
import practice10_theater_module
practice10_theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격 = 3명 가격은 30000원 입니다.
practice10_theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격 = 4명 조조 할인 가격은 24000원 입니다.
practice10_theater_module.price_soldier(5) # 5명이서 군인 할인 영화 보러 갔을 때 가격 = 5명 군인 할인 가격은 20000원 입니다.

import practice10_theater_module as mv # mv로 호출
mv.price(3) # 3명 가격은 30000원 입니다.
mv.price_morning(4) # 4명 조조 할인 가격은 24000원 입니다.
mv.price_soldier(5) # 5명 군인 할인 가격은 20000원 입니다.

from practice10_theater_module import *
price(3) # 3명 가격은 30000원 입니다.
price_morning(4) # 4명 조조 할인 가격은 24000원 입니다.
price_soldier(5) # 5명 군인 할인 가격은 20000원 입니다.

from practice10_theater_module import price, price_morning # 군인 할인 가격 필요 없을 경우
price(3) # 3명 가격은 30000원 입니다.
price_morning(4) # 4명 조조 할인 가격은 24000원 입니다.
# price_soldier(5) = 오류

from practice10_theater_module import price_soldier as price # 군인 할인 가격만 필요할 경우 / price로 호출
price(5) # 5명 군인 할인 가격은 20000원 입니다.



# 11-2 패키지 : 모듈을 모아 놓은 집합
import practice10_travel.thailand # import에서는 문장 맨 뒤가 모듈이나 패키지여야 함 (함수, 클래스 X)
trip_to = practice10_travel.thailand.ThailandPackage()
trip_to.detail() # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from practice10_travel.thailand import ThailandPackage # from import를 통해 문장 맨 뒤에 모듈, 패키지 및 함수나 클래스 사용 가능
trip_to = ThailandPackage()
trip_to.detail() # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from practice10_travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail() # [베트남 패키지 3박 5일] 다낭 효도 여행 60만원



# 11-3 __all__ : 패키지 내의 모듈에 대한 접근 권한 정의 (from import * 사용시)
from practice10_travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail() # [베트남 패키지 3박 5일] 다낭 효도 여행 60만원



# 11-4 모듈 직접 실행 : if __name__ == "__main__":을 활용하여 구분 가능 (thailand.py 참고)



# 11-5 패키지, 모듈 위치
import inspect # 모듈 위치 찾기
import random
print(inspect.getfile(random)) # random이라는 모듈이 어느위치에 있는지 파일정보 찾기 = C:\Python39\lib\random.py
print(inspect.getfile(thailand)) # c:\Users\Leessx\Desktop\PythonWorkspace\practice10_travel\thailand.py



# 11-6 pip install : pip로 패키지 설치하기

# 구글에 pypi검색 -> pypi.org접속(browse projects클릭(다양한 기준으로 찾기 가능)) -> beautifulsoup검색 -> beautifulsoup4클릭 -> pip install beautifulsoup4복사 -> 터미널 PS C:\Users\Leessx\Desktop\PythonWorkspace>뒤에 붙여 넣고 엔터 -> 예제 복붙해보기
'''from bs4 import BeautifulSoup
   soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
   print(soup.prettify())
     soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
   <p>
    Some
    <b>
     bad
     <i>
      HTML
     </i>
    </b>
   </p>'''

# PS C:\Users\Leessx\Desktop\PythonWorkspace> 뒤에 pip list 쓰기 : 패키지 내용 볼 수 있음
'''Package        Version
   -------------- -------
   beautifulsoup4 4.9.3
   pip            20.2.3
   setuptools     49.2.1
   soupsieve      2.2'''

# PS C:\Users\Leessx\Desktop\PythonWorkspace> 뒤에 pip show beautifulsoup4 쓰기 : beautifulsoup4에 대한 정보
'''Name: beautifulsoup4
   Version: 4.9.3
   Summary: Screen-scraping library
   Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
   Author: Leonard Richardson
   Author-email: leonardr@segfault.org
   License: MIT
   Location: c:\python39\lib\site-packages
   Requires: soupsieve
   Required-by:'''

# PS C:\Users\Leessx\Desktop\PythonWorkspace> 뒤에 pip install --upgrade beautifulsoup4 쓰기 : beautifulsoup4 최신버전으로 업그레이드 하기
'''Requirement already up-to-date: beautifulsoup4 in c:\python39\lib\site-packages (4.9.3)
   Requirement already satisfied, skipping upgrade: soupsieve>1.2; python_version >= "3.0" in c:\python39\lib\site-packages (from beautifulsoup4) (2.2)'''

# PS C:\Users\Leessx\Desktop\PythonWorkspace> 뒤에 pip uninstall beautifulsoup4 쓰기 : beautifulsoup4 설치제거 할지 y/n
'''Found existing installation: beautifulsoup4 4.9.3
   Uninstalling beautifulsoup4-4.9.3:
     Would remove:
       c:\python39\lib\site-packages\beautifulsoup4-4.9.3.dist-info\*
       c:\python39\lib\site-packages\bs4\*
   Proceed (y/n)? y
     Successfully uninstalled beautifulsoup4-4.9.3'''
   


# 11-7 내장 함수

# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?") # 무슨 언어를 좋아하세요? {0}입력
print("{0}은 아주 좋은 언어입니다.".format(language)) # {0}은 아주 좋은 언어입니다.

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) # ['ThailandPackage', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'inspect', 'language', 'mv', 'practice10_theater_module', 'practice10_travel', 'price', 'price_morning', 'price_soldier', 'random', 'thailand', 'trip_to', 'vietnam']
import random # 외장 함수
print(dir()) # ['ThailandPackage', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'inspect', 'language', 'mv', 'practice10_theater_module', 'practice10_travel', 'price', 'price_morning', 'price_soldier', 'random', 'thailand', 'trip_to', 'vietnam']
import pickle
print(dir()) # ['ThailandPackage', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'inspect', 'language', 'mv', 'pickle', 'practice10_theater_module', 'practice10_travel', 'price', 'price_morning', 'price_soldier', 'random', 'thailand', 'trip_to', 'vietnam']

print(dir(random)) # random모듈 내에서 쓸 수 있는 것들 뭐인지 = ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

lst = [1, 2, 3]
print(dir(lst)) # lst 내에서 쓸 수 있는 것들

name = "Jin"
print(dir(name)) # name 내에서 쓸 수 있는 것들

# 구글에 list of python builtins검색 -> Built-in Functions접속 -> 파이썬의 다양한 내장함수에 대한 정보 찾기 가능



# 11-8 외장 함수 : 직접 import하여 사용하는 것들

# 구글에 list of python modules검색 -> Python Module Index접속 -> 외장 함수 목록 열람 가능

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir과 같은 역할)
import glob
print(glob.glob("*py")) # 확장자가 py인 모든 파일 = ['helloworld.py', 'practice1.py', 'practice10.py', 'practice10_theater_module.py', 'practice2.py', 'practice3.py', 'practice4.py', 'practice5.py', 'practice6.py', 'practice7.py', 'practice8.py', 'practice9.py']

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 = C:\Users\Leessx\Desktop\PythonWorkspace

folder = "sample_dir"
if os.path.exists(folder): # 폴더 존재 여부 확인
   print("이미 존재하는 폴더입니다.") # 이미 존재하는 폴더입니다.
   os.rmdir(folder) # 폴더 삭제
   print(folder, "폴더를 삭제하였습니다.") # sample_dir 폴더를 삭제하였습니다.
else:
   os.makedirs(folder) # 폴더 생성
   print(folder, "폴더를 생성하였습니다.") # sample_dir 폴더를 생성하였습니다.

print(os.listdir()) # glob과 비슷하게 활용 = ['.vscode', 'helloworld.py', 'practice1.py', 'practice10.py', 'practice10_theater_module.py', 'practice10_travel', 'practice2.py', 'practice3.py', 'practice4.py', 'practice5.py', 'practice6.py', 'practice7.py', 'practice8.py', 'practice9.py', 'sample_dir', '__pycache__'] 

# time : 시간 관련 함수를 제공
import time
print(time.localtime()) # time.struct_time(tm_year=2021, tm_mon=2, tm_mday=21, tm_hour=13, tm_min=30, tm_sec=13, tm_wday=6, tm_yday=52, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 보기 쉽게 임의로 정렬 = 2021-02-21 13:31:30

import datetime
print("오늘 날짜는", datetime.date.today()) # 오늘 날짜는 2021-02-21

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘 날짜로 부터 100일 후 = 우리가 만난지 100일은 2021-06-01



# 11-9 Quiz
'''프로젝트 내에 나만의 시그지처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 practice10_byme.py로 작성

(모듈 사용 예제)
import practice10_byme
practice10_byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com'''

import practice10_byme
practice10_byme.sign()
'''이 프로그램은 나도코딩에 의해 만들어졌습니다.
   유튜브 : http://youtube.com
   이메일 : nadocoding@gmail.com'''