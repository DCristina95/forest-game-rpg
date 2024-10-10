import random

class Character:
    def __init__(self, species, xp, power):
        self.species = species
        self.xp = xp
        self.power = power

class Hero(Character):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)
        
    def runnaway(self):
        self.xp = self.xp - 50 
        
    def combat_oger(self): 
        opponent = Oger("oger", random.choice(range(10, 20)), 20) 
        while opponent.xp > 0 and self.xp > 0 and self.power > 0:
            attack_choice = int(input("\nQual o ataque que deseja usar: 1 ou 2? "))
            if attack_choice == 1:
                opponent.take_attack_1(self, attack_choice)
            elif attack_choice == 2:
                opponent.take_attack_2(self, attack_choice)
        if self.xp <= 0 or self.power <= 0:
            print("\n" + "GAME OVER"+ "\n")
            exit() 
    
    def combat_dragon(self): 
        opponent = Dragon("dragon", 50, 50)
        while opponent.xp > 0 and self.xp > 0 and self.power > 0:
            attack_choice = int(input("\nQual o ataque que deseja usar: 1 ou 2? "))
            if attack_choice == 1:
                opponent.take_attack_1(self, attack_choice)
            elif attack_choice == 2:
                opponent.take_attack_2(self, attack_choice)
        if self.xp <= 0 or self.power <= 0:
            print("\n" + "GAME OVER"+ "\n")
            exit() 

class Warrior(Hero):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)
        self.species = "warrior"
        self.xp = xp
        self.power = power
               
class Mage(Hero):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)
        self.species = "mage"
        self.xp = xp
        self.power = power
    

class Monster(Character):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)


class Oger(Monster):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)
        
    def take_attack_1(self, hero, attack):
        if hero.species == "mage" and attack == 1:
            self.xp = 0 
            hero.power = hero.power - self.power  
            print(f"O seu feitiço *Expeliarmus* foi eficaz contra o Ogre e conseguiu eliminá-lo! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power}")
        elif hero.species == "warrior" and attack == 1:
            hero.power = hero.power - 10  
            hero.xp = hero.xp - 30  
            self.xp = self.xp - 10 
            if self.xp > 0:
                print(f"O seu ataque de lança foi pouco eficaz contra o Ogre! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power} e o XP do Ogre é de {self.xp}")
            elif self.xp <= 0:
                print(f"\nAdversário derrotado. O seu XP é de: {hero.xp} e o seu power é de: {hero.power}.") 
    
    def take_attack_2(self, hero, attack): 
        if hero.species == "warrior" and attack == 2:
            hero.power = hero.power - self.power 
            self.xp = 0
            print(f"O seu ataque de espada foi eficaz contra o Ogre e conseguiu eliminá-lo! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power}")  
        elif hero.species == "mage" and attack == 2:
            hero.power = hero.power - 10 
            hero.xp = hero.xp - 20
            self.xp = self.xp - 10 
            if self.xp > 0:
                print(f"O seu feitiço *Avracadrava* foi pouco eficaz contra o Ogre! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power} o XP do Ogre é de {self.xp}") 
            elif self.xp <= 0:
                print(f"\nAdversário derrotado. O seu XP é de: {hero.xp} e o seu power é de: {hero.power}.") 

class Dragon(Monster):
    def __init__(self, species, xp, power):
        super().__init__(species, xp, power)
    
    def take_attack_1(self, hero, attack):
        if hero.species == "warrior" and attack == 1:
            hero.power = hero.power - self.power 
            self.xp = 0
            print(f"O seu ataque de lança foi eficaz contra o Dragão e conseguiu eliminá-lo! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power}") 
        elif hero.species == "mage" and attack == 1:
            hero.power = hero.power - 10 
            hero.xp = hero.xp - 20
            self.xp = self.xp - 10 
            if self.xp > 0:
                print(f"O seu feitiço *Expeliarmus* foi pouco eficaz contra o Dragão! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power} o XP do Dragão é de {self.xp}")        
            elif self.xp <= 0:
                print(f"\nAdversário derrotado. O seu XP é de: {hero.xp} e o seu power é de: {hero.power}.") 
   
    def take_attack_2(self, hero, attack):
        if hero.species == "mage" and attack == 2:
            self.xp = 0
            hero.power = hero.power - self.power   
            print(f"O seu feitiço *Avracadrava* foi eficaz contra o Dragão e conseguiu eliminá-lo! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power}")
        elif hero.species == "warrior" and attack == 2:
            hero.power = hero.power - 10   
            hero.xp = hero.xp - 30
            self.xp = self.xp - 10 
            if self.xp > 0:
                print(f"O seu ataque de espada foi pouco eficaz contra o Dragão! \nO seu XP é agora de {hero.xp} e o seu Power de {hero.power} e o XP do Dragão é de {self.xp}")
            elif self.xp <= 0:
                print(f"\nAdversário derrotado. O seu XP é de: {hero.xp} e o seu power é de: {hero.power}.") 


#colocar tudo o que é print no main 