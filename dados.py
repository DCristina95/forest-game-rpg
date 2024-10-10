
quest_1 = """'Após entrar na floresta, enquanto deambulava à sua descoberta, reparou que dentro
de um velho tronco de árvore algo parecia cintilar no seu interior... Quer explorar?'"""

quest_1_result_1 = """'Dentro do tronco econtra um cogumelo mágico que reconhece pelas sua capacidade
de aumentar o poder de quem o ingere! O seu Poder aumenta em 50!'"""

quest_1_result_2 = """'Ao virar-se para prosseguir o seu caminho, um ogre atravessa-se à sua frente 
repentinamente. Não há forma de o escapar!'"""

quest_2 = """'Você continua a sua viagem e observa o que parece ser um gigante ogre a atacar uma
pequena fada. Quando se aproxima para ver melhor, calca um ramo no chão e o barulho faz com que
o ogre o veja. Ele vem na sua direção!'"""

quest_2_if_win = """'Salvou a pequena fada! Como forma de gratidão ela recompensa-o com XP!'"""

quest_2_if_runnaway = """'Escapou, mas perdeu 50 de XP com o susto...'"""

quest_3 = """'Continua a sua jornada e finalmente avista a Torre Mágica! Dizem que a torre é
guardada por um Dragão, mas também que um enorme tesouro se encontra no seu interior. Você decide
entrar na torre. Ao explorar o seu interior, uma coluna de fogo desce do topo das escadas. É 
um Dragão! O que vai fazer?'"""

quest_3_if_win = """'Quando se aproxima do corpo do Dragão, repara que debaixo dele se encontra 
um baú fechado. Poderá este ser o tesouro? Você abre e vê que este se encontra repleto de barras de
ouro e jóias! A sua jornada chegou ao fim, mas não volta a casa de mãos vazias!'"""

quest_3_if_runnaway = """'Por pouco consegue escapar do Dragão... Consegue chegar ao fim da floresta
e regressar a casa. No entanto não consegue esquecer que talvez, dentro da Torre, houvesse mais
do que apenas o Dragão... Será que deveria voltar? Quem sabe poderia entrar numa nova aventura!'"""

quests = {
    "q_1": {"description": quest_1, "result_1": quest_1_result_1, "result_2": quest_1_result_2},
    "q_2": {"description": quest_2, "result_1": quest_2_if_win, "result_2": quest_2_if_runnaway},
    "q_3": {"description": quest_3, "result_1": quest_3_if_win, "result_2": quest_3_if_runnaway}
}

text_introduction_to_game = """
* * * Bemvindo! * * *
Este é o Jogo Descoberta da Floresta Encantada!
Neste jogo você irá explorar uma Floresta Encantada em após se ter perdido no retorno a casa.
Dizem que nesta floresta muitas criatura mágicas habitam... fadas, ogres e até dragões!
Há também rumores sobre uma torre onde se encontra um tesouro, mas são rumores apenas...
O seu objetivo à regressar a casa vivo, mas quem sabe...
Vamos partir à Aventura!
"""

text_rules = """Estas são as regras do jogo:
a) Um ataque eficaz elimina automaticamente o adversário, mas remove-lhe power igual ao power do adversário;
b) Um ataque ineficaz faz com que perca 10 de power e 30 de XP;
c) Um ataque ineficaz causa apenas um dano de 10 no xp do adversario;
d) Em caso de tentativa de fuga perde 50 de XP;
e) Se esgotar o seu power ou o seu XP, GAME OVER.
"""

text_character_options =  """
Vamos começar por escolher a sua personagem:
Warrior: XP = valor do dado x 12 / Power = valor do dado x 10
        Ataque 1: Ataque com Lança
        Ataque 2: Ataque com Espada
Mage: XP = valor do dado x 9 / Power = valor do dado x 13
        Ataque 1: Feitiço *Expeliarmus*
        Ataque 2: Feitiço *Avracadrava*
""" 

text_menu = """
-------------- MENU --------------
9) New Game;
8) Load Game; 
7) Save Game"""
#load e save não funcionam. Seriam aspetos a acrescentar e que viriam armazenar neste file
