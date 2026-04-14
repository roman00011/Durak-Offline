from random import *
from time import *
###########################################################################вывод карт#############################################################################
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
def print_all_card_tab(bot_cards,text,user_cards,text1):
    print_unknown_cards(bot_cards,text)
    print_cards(user_cards,text1)
#####################################################################################################################################################################################

def first_player_turn():     #первый ход игрока в цикле(помещение выбранных карт в layer_down и их удаление в прошлом хранилище)
    global layer_down
    global user_cards
    global trump_card
    print('выберите карты которыми хотите походить(номера карт через пробел пример: "1 3 5")')
    user_text=input()       #номер карты
    if len(user_text)==1:   #ход одной картой
        index_=int(user_text)-1
        layer_down.append(user_cards[index_])
        user_cards.pop(index_)
    else:                   #ход несколькими картами
        input_num_cards=list(map(int,user_text.split(' ')))
        similar_num=set([])
        for num_cards in input_num_cards:      #перебор номеров
            index_cards=num_cards-1            #номера становятся индексами
            if user_cards[index_cards][-2:]==trump_card[-2:]:  #если масть козырная
                user_cards_trump=int(user_cards[index_cards][0:-2])-20 # номер карты расшифровывается в нормальный вид
                similar_num.add(user_cards_trump)                      # и идет в сравнение
                layer_down.append(user_cards[index_cards])             # а в layer_down идет обычная карта
            else:                                              # если масть не козырная
                similar_num.add(int(user_cards[index_cards][0:-2]))    # номер карты идет в сравнение
                layer_down.append(user_cards[index_cards])             # а в layer_down идет обычная карта
        if len(similar_num)>1:          #проверка! если в сравнении номера карт разные то все начинается заново и layer_down обнуляется
            print('ебать ты шулер')
            print()
            layer_down.clear()
            first_player_turn()
            return
        for num_cards in input_num_cards:     # замена всех выбранных карт в картах игрока на '0'
            index_cards=num_cards-1
            user_cards.insert(index_cards,'0')
            user_cards.pop(index_cards+1)

        user_cards_alt=[]
        for card in user_cards:            #все остальное убирает '0' из карт игрока
            if card!='0':
                user_cards_alt.append(card)
        user_cards=user_cards_alt

def bot_defense_turn(): # реагирование бота на карты в layer_down и ответ на них. все карты идут в биту при отбивании
    global bot_cards
    global layer_down
    global layer_up
    global trump_card
    layer_down.sort(key=lambda x:x[0:-2])
    for selected_card in layer_down:      #карты из layer_down берутся и каждая прогоняется через алгоритм
        bot_cards=bot_defense_turn_utilite(selected_card,bot_cards) #обновление карт

    if len(layer_up)<len(layer_down):              # проверка на то если бот не отбился полностью от атаки в layer_down
        bot_cards.extend(layer_down)               # если не отбился то бот берет все карты из атаки (свои и чужие)
        bot_cards.extend(layer_up)
        layer_down.clear()
        layer_up.clear()
    elif len(layer_up)==len(layer_down):                                          # если отбился то все карты идут специальный слой для отбития
        discard_layer_down.extend(layer_down)
        discard_layer_up.extend(layer_up)
        layer_down.clear()
        layer_up.clear()
        
def bot_defense_turn_utilite(selected_card_layer_down,bot_cards):   #карты из layer_down берутся и каждая прогоняется через алгоритм
    global layer_up
    list_cards=[]
    for card in bot_cards:                 #берет карту из карт бота
        if selected_card_layer_down[-1]==card[-1] and int(selected_card_layer_down[0:-2])<int(card[0:-2]) or int(selected_card_layer_down[0:-2])<int(card[0:-2])-10 and selected_card_layer_down[0]!=card[0]:  #(если карта бота может победить карту игрока): если [масть] выбранной карты из layer_down [равна] [масти] выбранной карты из карт бота [и] [число] выбранной карты [меньше] чем [число] из карт бота [или] если одна [карт]а [обычная] а вторая [карта] [козырная]
            list_cards.append(card)                          #то помещает ее в отдельный список
    if len(list_cards)==0:
        return bot_cards
    if randint(0,2)>=1:
        list_cards.sort(key=lambda x:x[0:-2])             #обычный алгоритм: самая маленькая карта бьет другую самую маленькую карту
        layer_up.append(list_cards[0])
        bot_cards.remove(list_cards[0])
    else:
        random_index=randint(0,len(list_cards)-1)         #алгоритм рандома: из списка берется рандомная карта
        layer_up.append(list_cards[random_index])                        # в layer_up добавляется выбранная карта
        bot_cards.remove(list_cards[random_index])                       # и из карт бота она убирается

    return bot_cards                                 #обновление карт бота

def cycle_user_attack_check(discard_layer_up,discard_layer_down,user_cards):
    user_cards_sorting=[card[0:-2] for card in user_cards]
    user_cards_sorting_with_trump_card=[]
    discard_layer_duo=[]
    discard_layer_duo_sorting=[]
    discard_layer_duo_sorting_with_trump_card=[]
    discard_layer_duo.extend(discard_layer_down)
    discard_layer_duo.extend(discard_layer_up)
    discard_layer_duo_sorting = [card[0:-2] for card in discard_layer_duo]
    for card in user_cards_sorting:          #user_cards_sorting.sort(key=lambda x:int(x)-20 if int(x)>20 else int(x))
        if int(card)<20:
            user_cards_sorting_with_trump_card.append(card)
        else:
            user_cards_sorting_with_trump_card.append(str(int(card)-20))
    for card in discard_layer_duo_sorting:
        if int(card)<20:
            discard_layer_duo_sorting_with_trump_card.append(card)
        else:
            discard_layer_duo_sorting_with_trump_card.append(str(int(card)-20))
    variable=0
    for value in discard_layer_duo_sorting_with_trump_card:
        if value in user_cards_sorting_with_trump_card:
            variable+=1
    if variable>=1:
        return True
    else:
        return False



        
        
        
        


layer_down=[]                         #заданые переменные
layer_up=[]
discard_layer_down=[]
discard_layer_up=[]
cards_matrix=['1:Ч','2:Ч','3:Ч','4:Ч','5:Ч','6:Ч','7:Ч','8:Ч','9:Ч',
       '1:Б','2:Б','3:Б','4:Б','5:Б','6:Б','7:Б','8:Б','9:Б',
       '1:П','2:П','3:П','4:П','5:П','6:П','7:П','8:П','9:П',
       '1:К','2:К','3:К','4:К','5:К','6:К','7:К','8:К','9:К',]
cards = []
shuffle(cards_matrix)

trump_card=cards_matrix[0]       #задается козырь
del cards_matrix[0]

for card in cards_matrix:          # перебор карт и изменение числа козырей на n+20
    if card[-1] == trump_card[-1]:
        num_card = int(card[0:-2]) + 20
        cards.append(str(num_card) + card[-2:])
    else:
        cards.append(card)

trump_card=str(int(trump_card[0:-2])+20)+trump_card[-2:] # сам козырь тоже изменяется на n+20

user_cards=cards[0:6]   # берется 6 начальных карт из колоды для игрока
del cards[0:6]

bot_cards=cards[0:6]    # берется 6 начальных карт из колоды для бота
del cards[0:6]

bot_cards=['2:Ч','2:Б','2:П','22:К','23:К',]          #ЭТА НАДА УДАЛИТЬ
user_cards=['1:Ч','1:Б','1:П','21:К']        #ЭТА НАДА УДАЛИТЬ

while True:                            #цикл ходов
    print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:')
    print(f'Козырная карта - {trump_card}')
    print(f'discard_layer_up: {discard_layer_up}')          #ЭТА НАДА УДАЛИТЬ
    print(f'discard_layer_down: {discard_layer_down}')      #ЭТА НАДА УДАЛИТЬ
    print(f'layer_up: {layer_up}')                          #ЭТА НАДА УДАЛИТЬ
    print(f'layer_down: {layer_down}')                      #ЭТА НАДА УДАЛИТЬ
    print(f'user_cards: {user_cards}')                      #ЭТА НАДА УДАЛИТЬ
    print(f'bot_cards: {bot_cards}')                        #ЭТА НАДА УДАЛИТЬ
    first_player_turn()
    bot_defense_turn()
    print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:')
    user_can_attack=cycle_user_attack_check(discard_layer_up,discard_layer_down,user_cards)
    if user_can_attack:
        print('Ты можешь подкинуть карту, будешь делать?(да или нет)')
        user_command = input('---')
        if user_command.lower() == 'нет':
            user_can_attack = False
    while user_can_attack:
        print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:')
        first_player_turn()
        bot_defense_turn()
        print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:')
        user_can_attack=cycle_user_attack_check(discard_layer_up, discard_layer_down, user_cards)
        if user_can_attack:
            print('Ты можешь подкинуть карту, будешь делать?(да или нет)')
            user_command=input('---')
            if user_command.lower()=='нет':
                user_can_attack=False
    user_command=input('цикл атаки игрока окончен')