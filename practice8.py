# 9-1 클래스

from random import * # 403번째 줄을 위해

# 마린 : 공격 유닛, 군인, 총을 쓸 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력
print("{0}유닛이 생성되었습니다.".format(name)) # 마린유닛이 생성되었습니다.
print("체력은 {0}, 공격력 {1}\n".format(hp, damage)) # 체력은 40, 공격력 5

# 탱크 : 공격 유닛, 탱크, 포를 쓸 수 있음, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0}유닛이 생성되었습니다.".format(tank_name)) # 탱크유닛이 생성되었습니다.
print("체력은 {0}, 공격력 {1}\n".format(tank_hp, tank_damage)) # 체력은 150, 공격력 35

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35
print("{0}유닛이 생성되었습니다.".format(tank2_name)) # 탱크유닛이 생성되었습니다.
print("체력은 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage)) # 체력은 150, 공격력 35

def attack(name, location, damage):
    print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
    '''마린 : 1시방향으로 적군을 공격합니다. [공격력 5]
       탱크 : 1시방향으로 적군을 공격합니다. [공격력 35]
       탱크 : 1시방향으로 적군을 공격합니다. [공격력 35]'''

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 위의 과정을 클래스로 설정하기 
class Unit: # 클래스명 지정
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        '''마린유닛이 생성되었습니다.
           체력 40, 공격력 5
           마린유닛이 생성되었습니다.
           체력 40, 공격력 5
           탱크유닛이 생성되었습니다.
           체력 150, 공격력 35
           레이스유닛이 생성되었습니다.
           체력 80, 공격력 5
           빼앗은 레이스유닛이 생성되었습니다.
           체력 80, 공격력 5'''

marine1 = Unit("마린", 40, 5)
marine1 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)



# 9-2 __init__ : 생성자를 만들때 자동으로 호출



# 9-3 멤버변수 : 클래스 내에서 정의된 변수 ex) self.name, self.hp, self.damage

# 레이스 : 공격 유닛, 비행기, 클로킹(상대에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 유닛 이름 : 레이스, 공격력 : 5

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 추가적으로 변수를 만들어 씀

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name)) # 빼앗은 레이스는 현재 클로킹 상태입니다.



# 9-4 메소드 : 클래스에 해당하는 함수 추가 

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
    '''파이어뱃 : 5시방향으로 공격합니다. [공격력 16]
       파이어뱃 : 25데미지를 입었습니다.
       파이어뱃 : 현재 체력은 25입니다.
       파이어뱃 : 25데미지를 입었습니다.
       파이어뱃 : 현재 체력은 0입니다.
       파이어뱃 : 파괴되었습니다.'''

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)



# 9-5 상속 : 겹치는 클래스를 상속시키기(부모클래스 : Unit, 자식클래스 : AttackUint)

# 매딕 : 의무병, 공격력 없음(일반 유닛에서 데미지 필요 없음)
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage



# 9-6 다중 상속 : 콤마로 추가

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격기능 없음

# 날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도{2}]".format(name, location, self.flying_speed)) # 발키리 : 3시방향으로 날아갑니다. [속도5]

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")



# 9-7 메소드 오버라이딩 : 자식클래스에서 정의한 메소드를 쓰고 싶을 때

# 일반 유닛에 요소 추가
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]") # [지상 유닛 이동]
        print("{0} : {1}방향으로 이동합니다.".format(self.name, location, self.speed)) # 벌쳐 : 11시방향으로 이동합니다.

# Unit의 자식 클래스인 공격 유닛에도 추가
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도{2}]".format(name, location, self.flying_speed)) # 배틀크루저 : 9시방향으로 날아갑니다. [속도3]

# AttackUnit의 자식 클래스인 공중 공격 유닛 클래스 유닛에도 추가
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]") # [공중 유닛 이동]
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # FlyableAttackUnit에 def move메소드 추가하여 battlecruiser.fly(battlecruiser.name, "9시")를 대체함



# 9-8 pass

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 하지 않고 일단 넘어감

# 서플라이 디폿 : 건물, 1건물 당 8유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.") # [알림] 새로운 게임을 시작합니다.
    
def game_over():
    pass

game_start()
game_over()



# 9-9 super

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super()를 통해 초기화, Unit 불러옴, 다중 상속에서 문제
        self.location = location

# 다중 상속의 경우
class Unit:
    def __init__(self):
        print("Unit 생성자") # Unit 생성자

class Flyable:
    def __init__(self):
        print("Flyable 생성자") # Flyable 생성자

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() : 뒤에 있는 Flyable 출력안됨
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()



# 9-10 스타크래프트 프로잭트 전반전

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다.".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1}방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 공중 공격 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도{2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) 
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]") 
        self.fly(self.name, location)

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가
    seize_developed = False # 시즈모드 개발 여부
     
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return 

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        
        # 현재 시즈모드 일때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        
        # 클로킹 모드
        self.clocked = False # 클로킹 모드 해제 상태
    
    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        
        else: # 클로킹 모드 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True



# 9-11 스타크래프트 프로잭트 후반전

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player]님이 게임에서 퇴장하였습니다.")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = [] # 리스트 만들기
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # 현재 유닛의 클라스가 마린이면
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()



# 9-12 Quiz
'''주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass'''

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
        '''강남 아파트 매매 10억 2010년
           마포 오피스텔 전세 5억 2007년
           송파 빌라 월세 500/50 2000년'''

house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses = []
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses))) # 총 3대의 매물이 있습니다.
for house in houses:
    house.show_detail()