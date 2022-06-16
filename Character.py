class GameCharacter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    def is_alive(self):  #  살았는지 죽었는지
        return self.hp >0  #살아으면 True리턴

    def get_attacked(self, damage):
        if self.is_alive():
            self.hp = self.hp - damage if self.hp >= damage else 0
        else:
            print("{}님은 이미 죽었습니다.".format(self.name))
    def attack(self, other_character):
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        return self.name + "님의 hp는" + str(self.hp) + "만큼 남았습니다."

character_1 = GameCharacter("영훈전사", 200, 30)
character_2 = GameCharacter("지웅최고", 100, 50)

character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)
