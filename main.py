from model import Warrior, Mage
import random, os
from dados import quests, text_introduction_to_game, text_rules, text_character_options, text_menu

class Game():
    def __init__(self):
        self.player = None

    def print_introduction_to_game(self):
        print(text_menu)
        iniciate_game = int(input("Qual a sua opção? "))
        if iniciate_game == 9:
            os.system("clear")                  
            print(text_introduction_to_game)
            print(text_rules)
        
    def choose_character(self): 
        print(text_character_options)
        player_choice = int(input("Se quiser ser um Warrior pressione '1', se quiser ser um Mage pressione '2': "))
        print("\nVamos lançar o dados para atribuir o seu Power e o seu XP.\nDado lançado!")
        throw_dice_xp = random.choice(range(1,7))
        throw_dice_power = random.choice(range(1,7))
        if player_choice == 1:
            self.player = Warrior("warrior", 0, 0)
            self.player.xp = throw_dice_xp * 12
            self.player.power = throw_dice_power * 10
        elif player_choice == 2:
            self.player = Mage("mage", 0, 0)
            self.player.xp = throw_dice_xp * 9
            self.player.power = throw_dice_power * 13
        print(f"Você é um {self.player.species}, com XP:{self.player.xp} e Power:{self.player.power}")


    def play_game(self):
        new_game = int(input("\nPressione 1 para iniciar o jogo: "))
        if new_game == 1:
            os.system("clear")
            print("Let's Begin!") 
        print("\n" + quests["q_1"]["description"] + "\n")
        quest_1_choice = int(input("Se deseja explorar pressione 1, para continuar pressione 2: "))
        os.system("clear") 
        if quest_1_choice == 1:
            print("\n" + quests["q_1"]["result_1"])
            self.player.power = self.player.power + 50
        elif quest_1_choice == 2:
            print("\n" + quests["q_1"]["result_2"])
            self.player.combat_oger()
                
        
        print("\n" + quests["q_2"]["description"] + "\n")
        quest_2_choice = int(input("Se quiser enfrentar o Ogre pressione 1, se quiser tentar fugir pressione 2: "))
        os.system("clear") 
        if quest_2_choice == 1:
            self.player.combat_oger()
            self.player.xp = self.player.xp + 40
            print("\n" + quests["q_2"]["result_1"] + "\n" + f"O seu XP é agora de {self.player.xp}.")
        elif quest_2_choice ==2:
            print("\n" + quests["q_2"]["result_2"])
            self.player.runnaway()
            if self.player.xp <= 0:
                print("\n" + "GAME OVER"+ "\n")
                exit() 
        
        print("\n" + quests["q_3"]["description"] + "\n")
        quest_3_choice = int(input("Se deseja enfrentar o Dragão pressione 1, se deseja tentar fugir pressione 2: "))
        os.system("clear") 
        if quest_3_choice == 1:
            self.player.combat_dragon()
            print("\n" + quests["q_3"]["result_1"])
            print("\n" + "GAME COMPLETED")
        elif quest_3_choice == 2:
            print("\n" + quests["q_3"]["result_2"] + "\n")
            print("\n" + "GAME COMPLETED")
            


# EXECUTAR O JOGO:
game = Game()
game.print_introduction_to_game()
game.choose_character()
game.play_game()

