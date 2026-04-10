from random import *
from time import *
def print_cards(cards):
    len_cards=len(cards)
    p1=['     ___________']*len_cards   #s это '♠'   ♣ ♦ ♠ ♥
    p2=['    /v        /']*len_cards    #v это ' 9'  два символа
    p3=['    | s        |']*len_cards
    p4=['   /          / ']*len_cards
    p5=['  /     s    /  ']*len_cards
    p6=['  |          |  ']*len_cards
    p7=[' /       s  /   ']*len_cards
    p8=['/       v /    ']*len_cards
    p9=['|__________|    ']*len_cards
    p2_1=switch_cards_values(cards,p2,5)
    p8_1=switch_cards_values(cards,p8,8)
    p3_1=switch_cards_suit(cards,p3,6)
    p5_1=switch_cards_suit(cards,p5,8)
    p7_1=switch_cards_suit(cards,p7,9)
    print(unification(p1))
    print(unification(p2_1))
    print(unification(p3_1))
    print(unification(p4))
    print(unification(p5_1))
    print(unification(p6))
    print(unification(p7_1))
    print(unification(p8_1))
    print(unification(p9))
    print(f'Количество карт: {len_cards}')
    print()
def unification(p): #объединение списка слоев карт в красивый вид
    o='  '
    for i in p:
        o=o+' '+i
    o+='    '
    return o
def switch_cards_values(cards,p,s): # замена v на значения карт
    pp=[]
    for o in cards:
        for i in p:
            e=int(o[0])+5
            if e==10:
                e='10'
            elif e==11:
                e=' В'
            elif e==12:
                e=' Д'
            elif e==13:
                e=' К'
            elif e==14:
                e=' Т'
            else:
                e=' '+str(e)
            i=i[0:s]+e+i[s+1:]
            pp.append(i)
            break
    return pp
def switch_cards_suit(cards,p,s): # замена s на значения карт
    pp=[]
    for o in cards:
        for i in p:
            e=o[-1]
            if e =='Ч':
                e='♥'
            elif e =='П':
                e='♠'
            elif e =='К':
                e='♣'
            elif e =='Б':
                e='♦'
            i=i[0:s]+e+i[s+1:]
            pp.append(i)
            break
    return pp
def print_unknown_cards(cards):
    len_cards=len(cards)
    p1=['     ___________']*len_cards
    p2=['    /XXXXXXXXXX/']*len_cards
    p3=['    |XXXXXXXXXX|']*len_cards
    p4=['   /XXXXXXXXXX/ ']*len_cards
    p5=['  /XXXXXXXXXX/  ']*len_cards
    p6=['  |XXXXXXXXXX|  ']*len_cards
    p7=[' /XXXXXXXXXX/   ']*len_cards
    p8=['/XXXXXXXXXX/    ']*len_cards
    p9=['|XXXXXXXXXX|    ']*len_cards
    p0=['‾‾‾‾‾‾‾‾‾‾‾     ']*len_cards
    print(unification(p1))
    print(unification(p2))
    print(unification(p3))
    print(unification(p4))
    print(unification(p5))
    print(unification(p6))
    print(unification(p7))
    print(unification(p8))
    print(unification(p9))
    print(unification(p0))
    print(f'У противника {len(cards)} карт')
    print()
def cheats_command():
    global cheat_code
    global user_command
    if user_command.lower()=='показать карты бота' and cheat_code:
        print()
        print_cards(bot_cards)
    if user_command.lower()=='показать карты' and cheat_code:
        print('cards')
        print_cards(cards)
        print('bot_cards')
        print(bot_cards)
        print('battle_user')
        print(battle_user)
        print('battle_bot')
        print(battle_bot)
#def turn():
#    global cards
#    global battle_user
#    global battle_bot
#    global user_cards
#    global bot_cards
#    user_text=input()
#    if len(user_text)==1:
#        ui=int(user_text)-1
#        battle_user.append(user_cards[ui])
#        user_cards.pop(ui)
#    else:
#        indx=list(map(int,user_text.split(' ')))
#        s=set([])
#        d=[]
#        for i in indx:
#            ui=i-1
#            d.append(user_cards[ui][-2])
#            s.add(user_cards[ui][-2])
#            battle_user.append(user_cards[ui])
#        if len(s)>1:
#            print('ошибка, у карт разные цифры')
#            print()
#            battle_user.clear()
#            return
#        for i in sorted(indx, reverse=True):
#            ui=i-1
#            user_cards.pop(ui)
#def bot_turn():
#    global cards
#    global battle_bot
#    global bot_cards
#    global battle_user
#    btl_usr=battle_user
#    for i in btl_usr:              # карты которые я кинул                                                6 1 4
#        print('___________1__________',i)
#        for o in bot_cards:        # карты бота             пример: '♥ Червы:7 [2]','♥ Червы:10 [5]'               1 2 3 4 5 6 
#            print('___________2__________',o)
#            if i[2]==o[2] and i[-2]<o[-2]:
#                print('--------bu------------',battle_user, '___', i , o)
#                print('--------bc------------',bot_cards)
#                reserve.append(i)
#                reserve.append(o)
#                battle_user.remove(i)
#                bot_cards.remove(o)
#                print('--------bc2------------',bot_cards)
#                break
#    else:
#        print('reserve', reserve)
#        reserve.extend(battle_user)
#        bot_cards.extend(battle_user)
#        battle_user.clear()
cheat_code=False
battle_user=[]
battle_bot=[]
reserve=[]
tire='_'*200
cards=['1:Ч','2:Ч','3:Ч','4:Ч','5:Ч','6:Ч','7:Ч','8:Ч','9:Ч',
       '1:Б','2:Б','3:Б','4:Б','5:Б','6:Б','7:Б','8:Б','9:Б',
       '1:П','2:П','3:П','4:П','5:П','6:П','7:П','8:П','9:П',
       '1:К','2:К','3:К','4:К','5:К','6:К','7:К','8:К','9:К',]
tab=['Черви ♥','Бубы ♦','Пики ♠','Крести ♣']
shuffle(tab)
tab=tab[0]
shuffle(cards)
user_cards=cards[0:6]
del cards[0:6]
bot_cards=cards[0:6]
del cards[0:6]
while True:
    print(tire)
    if cheat_code:
        print('cheats on')
    print('Карты противника:')
    print_unknown_cards(bot_cards)
    print('Твои карты:')
    print_cards(user_cards)
    print(f'Козырная карта - {tab}')
    print('"стоп"-выключение игры')
    print()
    user_command=input()
    if user_command.lower()=='стоп':
        print('игра экстренно выключена')
        sleep(1)
        break
    if user_command.lower()=='читы67':
        if cheat_code:
            cheat_code=False
            continue
        cheat_code=True
    cheats_command()