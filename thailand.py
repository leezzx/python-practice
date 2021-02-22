class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__": # thailand.py에서 직접 실행하는 경우
    print("thailand모듈을 직접 실행") # thailand모듈을 직접 실행
    print("이 문장은 모듈을 직접 실행할 때만 실행되요.") # 이 문장은 모듈을 직접 실행할 때만 실행되요.
    trip_to = ThailandPackage()
    trip_to.detail() # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원
else: # practice10.py에서 ThailandPackage를 호출하여 사용하는 경우
    print("thailand 외부에서 모듈 호출") # thailand 외부에서 모듈 호출