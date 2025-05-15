from classes.game import Person, bcolors

magic = [
    {"name": "Fire","cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 17, "dmg": 90}
]
player = Person(460, 55, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)


running = True
# i = 0 
print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_magic()
    choice = input("Choose action: ")
    index = int(choice) - 1

    
    if index == 0:
        dmg = player.generate_demage()
        enemy.take_damage(dmg)
        print(f"You attacked for {dmg}, points of damage. Enemy HP: {enemy.get_hp()}")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choice magic: ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_mp_cost(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(f"{bcolors.FAIL} not enough MP {bcolors.ENDC}")
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)

        print(f"{bcolors.OKBLUE} {spell} deals {str(magic_dmg)} points of demage")

    
    enemy_choice = 1
    enemy_dmg = enemy.generate_demage()
    player.take_damage(enemy_dmg)
    print(f"Enemy attacks for : {enemy_dmg}, PLayer HP: {player.get_hp()}")


    if enemy.get_hp() == 0:
        print(f"{bcolors.OKBLUE} you WIN {bcolors.ENDC}")
        running = False
    elif player.get_hp() == 0:
        print(f"{bcolors.FAIL} Your enemy has defeated you {bcolors.ENDC}")
        running = False
