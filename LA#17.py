LA#17

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} and deals {self.attack_power} damage! {target.name} has only {target.health} hp remaining.")
        print("----------------")

       
angela = Player("Angela", 2000, 500)
ying = Player("Ying", 1500, 400)

print(f"{angela.name} HP: {angela.health} Attack Power: {angela.attack_power}")
print(f"{ying.name} HP: {ying.health} Attack Power: {ying.attack_power}\n")

angela.attack(ying)
print(f"{ying.name} HP: {ying.health} Attack Power: {ying.attack_power}")
ying.attack(angela)
print(f"{angela.name} HP: {angela.health} Attack Power: {angela.attack_power}")
angela.attack(ying)
print(f"{ying.name} HP: {ying.health} Attack Power: {ying.attack_power}")
ying.attack(angela)
print(f"{angela.name} HP: {angela.health} Attack Power: {angela.attack_power}")
angela.attack(ying)
print(f"{ying.name} HP: {ying.health} Attack Power: {ying.attack_power}")

print("\n")
if angela.health > ying.health:
    print("Angela is the WINNER!")
elif ying.health > angela.health:
    print("Ying is the WINNER!")
else:
    print("It's a DRAW!")
