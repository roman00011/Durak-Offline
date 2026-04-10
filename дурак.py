from random import *
from time import *
def show_user_cards():
        print('Твои карты:')
        #print('      1           2            3             4            5            6                    --- тестовая функция')
        print(user_cards)
        print(tire)

def turn():
    global cards
    global battle_user
    global battle_bot
    global user_cards
    global bot_cards
    user_text=input()
    if len(user_text)==1:
        ui=int(user_text)-1
        battle_user.append(user_cards[ui])
        user_cards.pop(ui)
    else:
        indx=list(map(int,user_text.split(' ')))
        s=set([])
        d=[]
        for i in indx:
            ui=i-1
            d.append(user_cards[ui][-2])
            s.add(user_cards[ui][-2])
            battle_user.append(user_cards[ui])
        if len(s)>1:
            print('ошибка, у карт разные цифры')
            print()
            battle_user.clear()
            return
        for i in sorted(indx, reverse=True):
            ui=i-1
            user_cards.pop(ui)
def bot_turn():
    global cards
    global battle_bot
    global bot_cards
    global battle_user
    btl_usr=battle_user
    for i in btl_usr:              # карты которые я кинул                                                6 1 4
        print('___________1__________',i)
        for o in bot_cards:        # карты бота             пример: '♥ Червы:7 [2]','♥ Червы:10 [5]'               1 2 3 4 5 6 
            print('___________2__________',o)
            if i[2]==o[2] and i[-2]<o[-2]:
                print('--------bu------------',battle_user, '___', i , o)
                print('--------bc------------',bot_cards)
                reserve.append(i)
                reserve.append(o)
                battle_user.remove(i)
                bot_cards.remove(o)
                print('--------bc2------------',bot_cards)
                break
    else:
        print('reserve', reserve)
        reserve.extend(battle_user)
        bot_cards.extend(battle_user)
        battle_user.clear()
                
                
    

    
    
    
    
        
    
    
    
cheat_code=False
battle_user=[]
battle_bot=[]
reserve=[]
tire='________________________________________________________________________________________________________________________________________________________________________'
cards=['♥ Червы:6 [1]','♥ Червы:7 [2]','♥ Червы:8 [3]','♥ Червы:9 [4]','♥ Червы:10 [5]','♥ Червы:В[6]','♥ Червы:Д [7]','♥ Червы:К [8]','♥ Червы:Т [9]',
   '♦ Бубны:6 [1]','♦ Бубны:7 [2]','♦ Бубны:8 [3]','♦ Бубны:9 [4]','♦ Бубны:10 [5]','♦ Бубны:В[6]','♦ Бубны:Д [7]','♦ Бубны:К [8]','♦ Бубны:Т [9]',
   '♠ Пики:6 [1]','♠ Пики:7 [2]','♠ Пики:8 [3]','♠ Пики:9 [4]','♠ Пики:10 [5]','♠ Пики:В[6]','♠ Пики:Д [7]','♠ Пики:К [8]','♠ Пики:Т [9]',
   '♣ Крести:6 [1]','♣ Крести:7 [2]','♣ Крести:8 [3]','♣ Крести:9 [4]','♣ Крести:10 [5]','♣ Крести:В[6]','♣ Крести:Д[7]','♣ Крести:К [8]','♣ Крести:Т [9]',]
tab=['♥','♦','♠','♣']
shuffle(tab)
tab=tab[0]
shuffle(cards)
user_cards=cards[0:6]
del cards[0:6]
bot_cards=cards[0:6]
del cards[0:6]
while True:
    if cheat_code:
        print('cheats on')
    print(f'у противника {len(bot_cards)} карт')
    print(f'козырь - {tab}')
    print('1-показать свои карты(если забыл), 2-сделать ход, "стоп"-выключение игры')
    print()
    user_command=input()
    if user_command.lower()=='стоп':
        print('игра экстренно выключена')
        sleep(1)
        break
    if user_command.lower()=='1':
        show_user_cards()
    if user_command.lower()=='2':
        print(tire)
        print(f'выбери карты 1-{len(user_cards)}, которыми будешь ходить(если если карт больше одной, пиши через пробел)')
        #print('      1               2               3               4                5               6                    --- тестовая функция')
        print(user_cards)
        turn()
        bot_turn()
    if user_command.lower()=='читы67':
        if cheat_code:
            cheat_code=False
            continue
        cheat_code=True
    if user_command.lower()=='показать карты бота' and cheat_code:
        print()
        print(bot_cards)
        print(tire)
    if user_command.lower()=='показать карты' and cheat_code:
        print('cards')
        print(cards)
        print('bot_cards')
        print(bot_cards)
        print('battle_user')
        print(battle_user)
        print('battle_bot')
        print(battle_bot)
        print(tire)
