import random

# 캐릭터 클래스


class BaseCharacter:
    def __init__(self, name, hp, power, mana=1):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mana = mana
        self.mana = mana
        self.power = power
        self.po_debuff = 0
        self.weak_debuff = 0
        self.vulunable_debuff = 0

    def attack(self, other):
        # 일반공격, 상대 취약 디버프시 1.5배 피해/ 자신 약화 디버프시 0.5배 피해
        if self.weak_debuff >= 1 and other.vulunable_debuff == 0:
            damage = random.randint(self.power - 4, self.power + 4)//2
        elif self.weak_debuff == 0 and other.vulunable_debuff >= 1:
            damage = int(random.randint(self.power - 4, self.power + 4)*1.5)
        else:
            damage = random.randint(self.power - 4, self.power + 4)

        # 적의 체력이 -로 표시되지 않게 max로 0과 비교해서 큰값 반환
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 타격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def sp_attack(self, other):
        # 특수공격, 마나 1소모, 상대에게 취약 디버프 2턴간 지속
        if self.mana == 0:
            print("스킬을 사용할 수 없습니다.")
        else:
            self.mana -= 1
            other.debuff_vulnerable(2)
            if self.weak_debuff >= 1 and other.vulunable_debuff == 0:
                damage = random.randint(self.power - 4, self.power + 4)//2
            elif self.weak_debuff == 0 and other.vulunable_debuff >= 1:
                damage = int(random.randint(
                    self.power - 4, self.power + 4)*1.5)
            else:
                damage = random.randint(self.power - 4, self.power + 4)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 강타! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")

    def sp_attack2(self, other):  # 2번째스킬
        pass

    def show_status(self):  # 상태 보여주기
        print(
            f"{self.name}의 상태: 체력 {self.hp}/{self.max_hp}\t 마나 {self.mana}/{self.max_mana}\n\t\t약화:{self.weak_debuff}턴\t취약{self.vulunable_debuff}턴")

    def recovery(self):  # 전투 종료 후 체력 회복
        self.hp = self.max_hp
        self.mana = self.max_mana

    def debuff_power(self, p_amount):  # 힘 감소 디버프
        self.po_debuff = p_amount
        self.power -= p_amount
        print("디버프에 걸렸습니다")
        print(
            f"{self.name}의 힘이 {p_amount}만큼 감소했습니다.\n({self.power} → {self.power - p_amount})")

    def debuff_vulnerable(self, v_duration):  # 취약 디버프 // 받는 피해 50% 증가
        self.vulunable_debuff += v_duration
        print(f"{self.name}는 {v_duration-1}턴간 취약에 걸렸습니다. 50%의 추가 피해를 입습니다!")

    def debuff_weak(self, w_duration):  # 약화 디버프 // 가하는 피해 50% 감소
        self.weak_debuff += w_duration
        print(f"{self.name}는 {w_duration-1}턴간 약화에 걸렸습니다. 가하는 피해가 50% 감소합니다!")

    def debuff_reset(self):  # 전투 종료 후 디버프 초기화
        self.power += self.po_debuff
        self.po_debuff = 0
        self.weak_debuff = 0
        self.vulunable_debuff = 0
        print(f"{self.name}의 상태가 회복되었습니다.")

    def debuff_reduce(self):  # 매턴 디버프 남은 시간 감소
        if self.vulunable_debuff >= 1:
            self.vulunable_debuff -= 1
        if self.weak_debuff >= 1:
            self.weak_debuff -= 1


# 캐릭터 클래스
class Character(BaseCharacter):
    def __init__(self, name, hp=800, power=10, mana=1):
        super().__init__(name, hp, power, mana)

        print(f'캐릭터의 이름은 {name}입니다.')


# 몬스터 클래스
class Monster(BaseCharacter):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self, other):
        atktype = random.randint(1, 4)
        if atktype > 1:
            if self.weak_debuff >= 1 and other.vulunable_debuff == 0:
                damage = random.randint(self.power - 4, self.power + 4)//2
            elif self.weak_debuff == 0 and other.vulunable_debuff >= 1:
                damage = int(random.randint(
                    self.power - 4, self.power + 4)*1.5)
            else:
                damage = random.randint(self.power - 4, self.power + 4)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print("GAME OVER")
        else:
            damage = random.randint(self.power, self.power + 5)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 강력한 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print("GAME OVER")

    def show_status(self):
        print(f"\n{self.name}의 상태: 체력 {self.hp}/{self.max_hp}")


# 1/콩벌레

class Louse(Monster):
    def __init__(self, name, hp=random.randint(10, 15), power=6):
        super().__init__(name, hp, power)


# 1/가시슬라임

class Spike_Slime(Monster):
    def __init__(self, name, hp=random.randint(10, 14), power=5):
        super().__init__(name, hp, power)

    def attack(self, other):
        atktype = random.randint(1, 4)
        if atktype > 1:
            if self.weak_debuff >= 1 and other.vulunable_debuff == 0:
                damage = random.randint(self.power - 4, self.power + 4)//2
            elif self.weak_debuff == 0 and other.vulunable_debuff >= 1:
                damage = int(random.randint(
                    self.power - 4, self.power + 4)*1.5)
            else:
                damage = random.randint(self.power - 4, self.power + 4)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print("GAME OVER")
        else:
            if self.hp < other.hp:
                other.debuff_weak(2)
            else:
                damage = random.randint(self.power, self.power + 5)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 치명타 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                if other.hp == 0:
                    print("GAME OVER")


# 1/광신도

class Cultist(Monster):
    def __init__(self, name, hp=random.randint(48, 53), power=6):
        super().__init__(name, hp, power)

    def attack(self, other):
        if self.weak_debuff >= 1 and other.vulunable_debuff == 0:
            damage = random.randint(self.power - 4, self.power + 4)//2
        elif self.weak_debuff == 0 and other.vulunable_debuff >= 1:
            damage = int(random.randint(self.power - 4, self.power + 4)*1.5)
        else:
            damage = random.randint(self.power - 4, self.power + 4)
        other.hp = max(other.hp - damage, 0)
        self.power += 2

        print(
            f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n {self.name}가 힘을 2얻었습니다.")
        if other.hp == 0:
            print("GAME OVER")


# 2/귀족 그렘린

class Gremlin_Nob(Monster):
    def __init__(self, name, hp=random.randint(82, 86), power=11):
        super().__init__(name, hp, power)

    def attack(self, other):
        atktype = random.randint(1, 4)
        if atktype > 1:
            damage = random.randint(self.power - 4, self.power + 4)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print("GAME OVER")
        else:
            self.power += 3
            damage = random.randint(self.power, self.power + 5)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name}이 격노합니다! {other.name}에게 {damage}의 데미지를 입혔습니다.\n{self.name}의 힘이 3 증가했습니다.")
            if other.hp == 0:
                print("GAME OVER")


# 2/라가불린

class Lagavulin(Monster):
    def __init__(self, name, hp=random.randint(109, 111), power=12):
        super().__init__(name, hp, power)

    def attack(self, other):
        atktype = random.randint(1, 3)
        if atktype > 1:
            damage = random.randint(self.power - 5, self.power + 4)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print("GAME OVER")
        else:
            if other.power >= 8:
                other.debuff_power(2)
            elif other.power >= 4:
                other.debuff_power(1)
            else:
                damage = random.randint(self.power - 5, self.power + 4)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                if other.hp == 0:
                    print("GAME OVER")

# boss/육각령


class Hexaghost(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
