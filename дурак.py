from random import *
from time import *
#                                                    вывод карт
#####################################################################################################################################################################################
def print_cards(cards,text):
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
def print_all_card_tab(bot_cards,text,user_cards,text1,layer_down,discard_layer_up,discard_layer_down):
    global trump_card
    print_unknown_cards(bot_cards,text)
    print_battle_cards(layer_down, discard_layer_up, discard_layer_down)
    print_cards(user_cards,text1)
    print(f'Козырная карта - {trump_card}')

def print_battle_cards(layer_down_cards,discard_up_cards,discard_down_cards):
    len_discard_cards=len(discard_up_cards)
    len_cards=len(layer_down_cards)
    p1 =['     ___________   ']*len_discard_cards      #на пару значений передвинуть вправо
    p2 =['    /v        /___']*len_discard_cards
    p3 =['    | s        |  /']*len_discard_cards
    p4 =['   /          /   |']*len_discard_cards
    p5 =['  /     s    /   / ']*len_discard_cards
    p6 =['  |          |  /  ']*len_discard_cards
    p7 =[' /       s  /   |  ']*len_discard_cards
    p8 =['/       v / S /   ']*len_discard_cards
    p9 =['|__________|V/    ']*len_discard_cards
    p10=['   |__________|    ']*len_discard_cards
    p2_1=switch_cards_values(discard_up_cards, p2, 5)
    p8_1=switch_cards_values(discard_up_cards, p8, 8)
    p8_2=switch_cards_suit(discard_down_cards,p8_1,13)
    p9_1=switch_cards_values(discard_down_cards,p9,12)
    p3_1=switch_cards_suit(discard_up_cards, p3, 6)
    p5_1=switch_cards_suit(discard_up_cards,p5,8)
    p7_1=switch_cards_suit(discard_up_cards,p7,9)

    p2_alt = ['     ___________'] * len_cards
    p3_alt = ['    /v        /'] * len_cards
    p4_alt = ['    | s        |'] * len_cards
    p5_alt = ['   /          / '] * len_cards
    p6_alt = ['  /     s    /  '] * len_cards
    p7_alt = ['  |          |  '] * len_cards
    p8_alt = [' /       s  /   '] * len_cards
    p9_alt = ['/       v /    '] * len_cards
    p10_alt = ['|__________|    '] * len_cards
    p3_alt_1 = switch_cards_values(layer_down_cards, p3_alt, 5)
    p9_alt_1 = switch_cards_values(layer_down_cards, p9_alt, 8)
    p4_alt_1 = switch_cards_suit(layer_down_cards, p4_alt, 6)
    p6_alt_1 = switch_cards_suit(layer_down_cards, p6_alt, 8)
    p8_alt_1 = switch_cards_suit(layer_down_cards, p8_alt, 9)

    p2_1.extend(p2_alt)
    p3_1.extend(p3_alt_1)
    p4.extend(p4_alt_1)
    p5_1.extend(p5_alt)
    p6.extend(p6_alt_1)
    p7_1.extend(p7_alt)
    p8_2.extend(p8_alt_1)
    p9_1.extend(p9_alt_1)
    p10.extend(p10_alt)

    print(unification(p1))
    print(unification(p2_1))
    print(unification(p3_1))
    print(unification(p4))
    print(unification(p5_1))
    print(unification(p6))
    print(unification(p7_1))
    print(unification(p8_2))
    print(unification(p9_1))
    print(unification(p10))
    print()
#####################################################################################################################################################################################

def first_player_turn():     #первый ход игрока в цикле(помещение выбранных карт в layer_down и их удаление в прошлом хранилище)
    global layer_down
    global user_cards
    global discard_layer_up
    global discard_layer_down
    discard_layer_duo = []
    discard_layer_duo.extend(discard_layer_up)
    discard_layer_duo.extend(discard_layer_down)
    print('выберите карты которыми хотите походить(номера карт через пробел пример: "1 3 5")')      #игрок может поставить те карты, значение которых есть в discard_layer_down и discard_layer_up
    user_text=input()       #номер карты
    if len(user_text)==1:   #ход одной картой
        index_=int(user_text)-1
        discard_layer_duo=[]
        discard_layer_duo_sorting_with_trump_card=[]
        discard_layer_duo.extend(discard_layer_up)
        discard_layer_duo.extend(discard_layer_down)
        discard_layer_duo_sorting = [card[0:-2] for card in discard_layer_duo]
        user_card = []
        if int(user_cards[index_][0:-2])>20:                     #перевод козырных карт
            user_card.append(str(int(user_cards[index_][0:-2])-20))
        else:
            user_card.append(str(int(user_cards[index_][0:-2])))

        for card in discard_layer_duo_sorting:                   #перевод козырных карт
            if int(card) < 20:
                discard_layer_duo_sorting_with_trump_card.append(card)
            else:
                discard_layer_duo_sorting_with_trump_card.append(str(int(card) - 20))

        if user_card[0] not in discard_layer_duo_sorting_with_trump_card and len(discard_layer_duo)>0: # если значения карты нету в discard и если в discard есть карты
            print('ебать ты шулер')
            print(discard_layer_duo_sorting_with_trump_card, user_card[0])
            first_player_turn()
            return
        layer_down.append(user_cards[index_])
        user_cards.pop(index_)
    else:                   #ход несколькими картами
        input_num_cards=list(map(int,user_text.split(' ')))
        discard_layer_duo = []
        discard_layer_duo_sorting_with_trump_card = []
        user_card = []
        user_card_sorted=[]
        discard_layer_duo.extend(discard_layer_up)
        discard_layer_duo.extend(discard_layer_down)
        discard_layer_duo_sorting = [card[0:-2] for card in discard_layer_duo]
        for card in discard_layer_duo_sorting:                   #перевод козырных карт
            if int(card) < 20:
                discard_layer_duo_sorting_with_trump_card.append(card)
            else:
                discard_layer_duo_sorting_with_trump_card.append(str(int(card) - 20))
        user_text_indexes = [i - 1 for i in input_num_cards]
        variable=0
        for card_i in  user_text_indexes:
            user_card.append(user_cards[card_i][0:-2])

        for card in user_card:                   #перевод козырных карт
            if int(card) < 20:
                user_card_sorted.append(card)
            else:
                user_card_sorted.append(str(int(card) - 20))

        for card in user_card_sorted:
            if card in discard_layer_duo_sorting_with_trump_card and len(discard_layer_duo)>0:
                variable+=1



        similar_num=set([])
        if len(discard_layer_duo)==0 or variable==0:        #надо делать если discard равен нулю или если
            for num_cards in input_num_cards:      #перебор номеров
                index_cards=num_cards-1            #номера становятся индексами
                if user_cards[index_cards][-2:]==trump_card[-2:]:  #если масть козырная
                    user_cards_trump=int(user_cards[index_cards][0:-2])-20 # номер карты расшифровывается в нормальный вид
                    similar_num.add(user_cards_trump)                      # и идет в сравнение
                    layer_down.append(user_cards[index_cards])             # а в layer_down идет обычная карта
                else:                                              # если масть не козырная
                    similar_num.add(int(user_cards[index_cards][0:-2]))    # номер карты идет в сравнение
                    layer_down.append(user_cards[index_cards])             # а в layer_down идет обычная карта
        else:
            for num_cards in input_num_cards:
                index_cards = num_cards - 1
                layer_down.append(user_cards[index_cards])
        if len(similar_num)>1 or (variable!=len(input_num_cards) and len(discard_layer_duo)>0):          #проверка! если в сравнении номера карт разные то все начинается заново и layer_down обнуляется                            ОШИБКА !!!!!!!!!!
            print('ебать ты шулер')
            print(variable)
            print()
            layer_down.clear()
            first_player_turn()
            return
        for num_cards in input_num_cards:     # замена всех выбранных карт в картах игрока на '0'
            index_cards=num_cards-1
            user_cards.insert(index_cards,'0')
            user_cards.pop(index_cards+1)

        user_cards_none_0=[]
        for card in user_cards:            #все остальное убирает '0' из карт игрока
            if card!='0':
                user_cards_none_0.append(card)
        user_cards=user_cards_none_0

def bot_defense_turn(): # реагирование бота на карты в layer_down и ответ на них. все карты идут в биту при отбивании
    global bot_cards
    global layer_down
    global layer_up
    print('Бот думает')
    sleep(1.75)
    layer_down.sort(key=lambda x:x[0:-2])
    for selected_card in layer_down:      #карты из layer_down берутся и каждая прогоняется через алгоритм
        bot_cards=bot_defense_turn_utilite(selected_card,bot_cards) #обновление карт

    if len(layer_up)<len(layer_down):              # проверка на то если бот не отбился полностью от атаки в layer_down
        bot_cards.extend(layer_down)               # если не отбился то бот берет все карты из атаки (свои и чужие)
        bot_cards.extend(layer_up)
        bot_cards.extend(discard_layer_down)
        bot_cards.extend(discard_layer_up)
        discard_layer_down.clear()
        discard_layer_up.clear()
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
    if randint(1,4)>=2:
        list_cards.sort(key=lambda x:x[0:-2])             #обычный алгоритм: самая маленькая карта бьет другую самую маленькую карту
        layer_up.append(list_cards[0])
        bot_cards.remove(list_cards[0])
    else:
        random_index=randint(0,len(list_cards)-1)         #алгоритм рандома: из списка берется рандомная карта
        layer_up.append(list_cards[random_index])                        # в layer_up добавляется выбранная карта
        bot_cards.remove(list_cards[random_index])                       # и из карт бота она убирается

    return bot_cards                                 #обновление карт бота

def cycle_user_attack_check(discard_layer_up,discard_layer_down,user_card):    #если каждое значение карты user_cards есть в discard_layer_duo то да, иначе нет
    user_cards_sorting = [card[0:-2] for card in user_card]
    user_cards_sorting_with_trump_card=[]
    discard_layer_duo=[]
    discard_layer_duo_sorting=[]
    discard_layer_duo_sorting_with_trump_card=[]
    discard_layer_duo.extend(discard_layer_down)
    discard_layer_duo.extend(discard_layer_up)
    discard_layer_duo_sorting = [card[0:-2] for card in discard_layer_duo]

    for card_u in user_cards_sorting:
        if int(card_u)<20:
            user_cards_sorting_with_trump_card.append(card_u)
        else:
            user_cards_sorting_with_trump_card.append(str(int(card_u)-20))
    for card in discard_layer_duo_sorting:
        if int(card)<20:
            discard_layer_duo_sorting_with_trump_card.append(card)
        else:
            discard_layer_duo_sorting_with_trump_card.append(str(int(card)-20))
    variable=0
    for value in user_cards_sorting_with_trump_card:
        if value in discard_layer_duo_sorting_with_trump_card:
            variable+=1
    if variable>=1:
        return True
    else:
        return False

layer_up=[]
layer_down=[]                         #заданые переменные
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

trump_card='6:К'                                        #ЭТА НАДА УДАЛИТЬ

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

bot_cards=['23:К','23:К','23:К']                           #ЭТА НАДА УДАЛИТЬ
user_cards=['1:Ч','1:Б','2:Ч','22:К','3:П']                 #ЭТА НАДА УДАЛИТЬ
#layer_up=[]                                                  #ЭТА НАДА УДАЛИТЬ
#layer_down=[]                                               #ЭТА НАДА УДАЛИТЬ
#discard_layer_down=[]                                        #ЭТА НАДА УДАЛИТЬ
#discard_layer_up=[]                                         #ЭТА НАДА УДАЛИТЬ

while True:                            #цикл ходов
    bot_cards_len_before=len(bot_cards)
    print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:',layer_down,discard_layer_up,discard_layer_down)
    first_player_turn()
    print_all_card_tab(bot_cards, '                 Карты противника:', user_cards, '                 Твои карты:',layer_down, discard_layer_up, discard_layer_down)
    bot_defense_turn()
    print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:',layer_down,discard_layer_up,discard_layer_down)
    bot_cards_len_after = len(bot_cards)
    if bot_cards_len_before>bot_cards_len_after:
        user_can_attack=cycle_user_attack_check(discard_layer_up,discard_layer_down,user_cards)
    else:
        user_can_attack=True
    if user_can_attack and bot_cards_len_before < bot_cards_len_after:
        print('Ты можешь сделать ход еще раз ')
        sleep(1.75)
    elif user_can_attack:
        print('Ты можешь сделать ход еще раз ("нет" если не будешь,остальные символы означают "да")')
        user_command = input('---')
        if user_command.lower() == 'нет':
            user_can_attack = False

    while user_can_attack:
        bot_cards_len_before = len(bot_cards)
        print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        first_player_turn()
        print_all_card_tab(bot_cards, '                 Карты противника:', user_cards, '                 Твои карты:',layer_down, discard_layer_up, discard_layer_down)
        bot_defense_turn()
        print_all_card_tab(bot_cards,'                 Карты противника:',user_cards,'                 Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        bot_cards_len_after = len(bot_cards)
        if bot_cards_len_before > bot_cards_len_after:
            user_can_attack = cycle_user_attack_check(discard_layer_up, discard_layer_down, user_cards)
        else:
            user_can_attack = True
        if user_can_attack and bot_cards_len_before<bot_cards_len_after:
            print('Ты можешь сделать ход еще раз ')
        elif user_can_attack:
            print('Ты можешь сделать ход еще раз ("нет" если не будешь,остальные символы означают "да")')
            user_command=input('---')
            if user_command.lower()=='нет':
                user_can_attack=False
    print()
    user_command=input('цикл атаки игрока окончен')