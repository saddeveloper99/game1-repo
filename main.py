from classes import *
import random

stage = 1

print("\n닉네임을 입력해주세요")
name = str(input(""))

player = Character(name)

Enemychoice = random.randint(1, 3)
# Enemychoice = 2
if Enemychoice == 1:
    monster = Louse(name="콩벌레")

elif Enemychoice == 2:
    monster = Spike_Slime(name="가시슬라임")

elif Enemychoice == 3:
    monster = Cultist(name="광신도")

while stage == 1:
    if monster.hp > 0 and player.hp > 0:
        print(f"\n{monster.name}과(와)의 전투! 무엇을 할까?")
        monster.show_status()
        print("1.일반공격 2.특수공격 3.턴 넘기기")
        move = int(input(""))
        if move == 1:
            player.attack(monster)
            if monster.hp > 0:
                monster.attack(player)
            monster.show_status()
            player.debuff_reduce()
            player.show_status()

        elif move == 2:
            if player.mana == 0:
                print("\n** 마나가 부족해 스킬을 사용할 수 없습니다 **")
            else:
                player.sp_attack(monster)
                if monster.hp > 0:
                    monster.attack(player)
                monster.show_status()
                player.debuff_reduce()
                player.show_status()

        elif move == 3:
            monster.attack(player)
            monster.show_status()
            player.debuff_reduce()
            player.show_status()
        else:
            print("입력오류")
            continue

    elif player.hp <= 0:
        print("당신은 패배했습니다...")
        break
    else:
        stage += 1
        player.max_mana += 1
        player.power += 2
        player.recovery()
        player.debuff_reset()
        print("\n승리했습니다!")
        print("\n  2 STAGE  ")


Enemychoice2 = Enemychoice = random.randint(1, 2)

if Enemychoice2 == 1:
    monster = Gremlin_Nob(name="귀족 그렘린")

elif Enemychoice2 == 2:
    monster = Lagavulin(name="라가불린")

while stage == 2:
    if monster.hp > 0 and player.hp > 0:
        print(f"\n{monster.name}과(와)의 전투! 무엇을 할까?")
        monster.show_status()
        print("\n1.일반공격 2.특수공격 3.턴 넘기기")
        move = int(input(""))
        if move == 1:
            player.attack(monster)
            if monster.hp > 0:
                monster.attack(player)
            monster.show_status()
            player.debuff_reduce()
            player.show_status()

        elif move == 2:
            if player.mana == 0:
                print("\n** 마나가 부족해 스킬을 사용할 수 없습니다 **")
            else:
                player.sp_attack(monster)
                if monster.hp > 0:
                    monster.attack(player)
                monster.show_status()
                player.debuff_reduce()
                player.show_status()

        elif move == 3:
            monster.attack(player)
            monster.show_status()
            player.debuff_reduce()
            player.show_status()
        else:
            print("입력오류")
            continue

    elif player.hp <= 0:
        print("당신은 패배했습니다...")
        break

    else:
        stage += 1
        # player.max_mana += 1
        # player.power += 2
        # player.recovery()
        # player.debuff_reset()
        print("승리했습니다!")
        break
