import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp 
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Atack", "Magic"]


    def generate_demage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mql = self.magic[i]["dmg"] - 5
        ngh = self.magic[i]["dmg"] + 5
        return random.randrange(mql, ngh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
           self.hp = 0 
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxhp
    
    def reduce_mp(self, cost):
        self.mp  -= cost
        
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(f"{i}: {item}")
            i += 1

    def choose_magic(self):
        print("\n--- Available Spells ---")

        for i, spell in enumerate(self.magic, start=1):
            print(f"{i}: {spell['name']} (Cost: {spell['cost']} MP)")


