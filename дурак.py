from random import *
from time import *
def first_player_turn():
    global layer_down
    global user_cards
    global trump_card
    print('выберите карты которыми хотите походить(номера карт через пробел пример: "1 3 5")')
    user_text=input()
    if len(user_text)==1:
        index_=int(user_text)-1
        layer_down.append(user_cards[index_])
        user_cards.pop(index_)
    else:
        indexes_=list(map(int,user_text.split(' ')))
        n=set([])
        for i in indexes_:
            ui=i-1
            if user_cards[ui][-2:]==trump_card[-2:]:
                usr_crds=int(user_cards[ui][0:-2])-20
                n.add(usr_crds)
                layer_down.append(user_cards[ui])
            else:
                n.add(int(user_cards[ui][0:-2]))
                layer_down.append(user_cards[ui])
        if len(n)>1:
            print('ебать ты шулер')
            print()
            layer_down.clear()
            first_player_turn()
            return
        for i in indexes_:
            ui=i-1
            user_cards.insert(ui,'0')
            user_cards.pop(ui+1)
        user_cards_=[]
        for i in user_cards:
            if i!='0':
                user_cards_.append(i)
        user_cards=user_cards_
        
def bot_defense_turn():
    global bot_cards
    global layer_down
    global layer_up
    global trump_card
    ld=len(layer_down)


    for i in layer_down:
        bot_cards=bot_defense_turn_utilite(i,bot_cards)

    if len(layer_up)<ld:
        bot_cards.extend(layer_down)
        bot_cards.extend(layer_up)
        layer_down.clear()
        layer_up.clear()
    else:
        discard_layer_down.extend(layer_down)
        layer_down.clear()
        discard_layer_up.extend(layer_up)
        layer_up.clear()
        
def bot_defense_turn_utilite(i,bot_cards):
    global layer_down
    global layer_up
    #print(f'layer_down: {layer_down}')
    #print(f'bot_cards: {bot_cards}')
    #print()
    l1=len(bot_cards)
    for o in bot_cards:
        if i[-1]==o[-1] and int(i[0:-2])<int(o[0:-2]) or int(i[0:-2])<int(o[0:-2])-10:   
            layer_up.append(o)
            bot_cards.remove(o)
            return bot_cards
    l2=len(bot_cards)
    if l2==l2:
        return bot_cards

            
        
        
        
        
        
    
    
    
def check_trump_card(card):
    global trump_card
    cards=[]
    for y in card:
        if y[-1]==trump_card[-1]:
            tr=int(y[0:-2])+20
            cards.append(str(tr)+y[-2:])
        else:
            cards.append(y)
    return cards
            
def print_cards(cards,text):
    global trump_card
    print(text)
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
    print(f'                 Количество карт: {len_cards}')
    print()
def unification(p): #объединение списка слоев карт в красивый вид без списков
    o='                 '
    for i in p:
        o=o+' '+i
    o+='    '
    return o
def switch_cards_values(cards,p,s): # замена v на значения карт
    global trump_card
    pp=[]
    for o in cards:
        for i in p:
            e=int(o[0:-2])+5
            if e==10:
                e='10'
            elif e==11 or e==31:
                e=' В'
            elif e==12 or e==32:
                e=' Д'
            elif e==13 or e==33:
                e=' К'
            elif e==14 or e==34:
                e=' Т'
            elif e==26:
                e=' '+'6'
            elif e==27:
                e=' '+'7'
            elif e==28:
                e=' '+'8'
            elif e==29:
                e=' '+'9'
            elif e==30:
                e='10'
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
def print_unknown_cards(cards,text):
    print(text)
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
    print(f'                 У противника {len(cards)} карт')
    print()
def tire():
    for i in range(20):
        print()
        
layer_down=[]
layer_up=[]
discard_layer_down=[]
discard_layer_up=[]
cards_matrix=['1:Ч','2:Ч','3:Ч','4:Ч','5:Ч','6:Ч','7:Ч','8:Ч','9:Ч',
       '1:Б','2:Б','3:Б','4:Б','5:Б','6:Б','7:Б','8:Б','9:Б',
       '1:П','2:П','3:П','4:П','5:П','6:П','7:П','8:П','9:П',
       '1:К','2:К','3:К','4:К','5:К','6:К','7:К','8:К','9:К',]
shuffle(cards_matrix)

trump_card=cards_matrix[0] #+20
del cards_matrix[0]

cards=check_trump_card(cards_matrix)

trump_c=int(trump_card[0:-2])+20
trump_card=str(trump_c)+trump_card[-2:]

user_cards=cards[0:6]
del cards[0:6]
bot_cards=cards[0:6]
del cards[0:6]
bot_cards=['29:К','28:К','8:Ч','5:К','7:П','9:П']         #DELETE
user_cards=['1:Ч','1:Б','1:П','2:П','21:К','22:К',] #DELETE

while True:
    print(cards)
    tire()
    print_unknown_cards(bot_cards,'                 Карты противника:')
    print_cards(user_cards,'                 Твои карты:')
    print(f'Козырная карта - {trump_card}')
    print(f'discard_layer_up: {discard_layer_up}')
    print(f'discard_layer_down: {discard_layer_down}')
    print('"стоп"-выключение игры')
    print(f'user_cards: {user_cards}')
    print(f'bot_cards: {bot_cards}')
    first_player_turn()
    bot_defense_turn()
    user_command=input('---')
    if user_command.lower()=='стоп':
        print('игра экстренно выключена')
        sleep(1)
        break