wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

print("1) ", wizard)
print("2) ", elf)
print("3) ", human)

while True:
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen: " + wizard)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen: " + elf)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chosen: " + human)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    else:
        print("Uknown Character")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "has damaged the Dragon!")
    if dragon_hp <= 0:
        print("The Dragon's hitpoints are now at: " + str(dragon_hp))
        print("The Dragon has lost the battle!")
        break
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    my_hp = my_hp - dragon_damage
    print("The Dragon has damaged the " + character + "! ")
    print(character + " now has " + str(my_hp) + " hitpoints left. ")
    if my_hp <= 0:
        print(character, "has lost the battle!")
        break
