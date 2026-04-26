import os
from random import *
from time import *
#                                                                          вывод карт
#####################################################################################################################################################################################


def print_cards(cards,text):
    print('                           '+text)
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
    p0=['[    X    ]    ']*len_cards
    p2_1=switch_cards_values(cards,p2,5)
    p8_1=switch_cards_values(cards,p8,8)
    p3_1=switch_cards_suit(cards,p3,6)
    p5_1=switch_cards_suit(cards,p5,8)
    p7_1=switch_cards_suit(cards,p7,9)
    p0_0=count_num_user_cards(p0,5)
    print(unification(p1))
    print(unification(p2_1))
    print(unification(p3_1))
    print(unification(p4))
    print(unification(p5_1))
    print(unification(p6))
    print(unification(p7_1))
    print(unification(p8_1))
    print(unification(p9))
    print('              Номера:'+battle_unification(p0_0))
    print()


def unification(p): #объединение списка слоев карт в красивый вид без списков
    o='                      '
    for i in p:
        o=o+' '+i
    o+='    '
    return o


def count_num_user_cards(p,s):
    number=1
    pp=[]
    for i in p:
        if number<10:
            number_s=' '+str(number)
        else:
            number_s=str(number)
        pp.append(i[0:s]+number_s+i[s+1:])
        number+=1
    return pp


def unification_alt(p): #объединение списка слоев карт в красивый вид без списков
    o='     '
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


def switch_cards_suit_alt(cards,p,s): # замена s на значения карт
    pp=[]
    uuu=0
    for i in p:
        o=cards[uuu]
        uuu+=1
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
    return pp


def print_unknown_cards(cards,text):        # карты противника
    print('                           '+text)
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
    print(f'                       Количество карт противника: {len(cards)}')
    print()


def print_all_card_tab(bot_cards,text,user_cards,text1,layer_down,discard_layer_up,discard_layer_down):
    #for i in range(10):
    #    print()
    os.system('cls')
    print_unknown_cards(bot_cards,text)
    print_battle_cards(layer_down, discard_layer_up, discard_layer_down)
    print_cards(user_cards,text1)


def battle_unification(p):
    o = ''
    for i in p:
        o = o + ' ' + i
    o += ' '
    return o


def switch_cards_len(p, s):  # замена s на значения карт
    global cards
    pp = []
    if len(cards)<10:
        i=' '+str(len(cards))
    else:
        i=str(len(cards))
    o=p[0][0:s]+i+p[0][s+1:]
    pp.append(o)
    return pp


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
    p0 =['                   ']*len_discard_cards
    p2_1=switch_cards_values(discard_up_cards, p2, 5)
    p8_1=switch_cards_values(discard_up_cards, p8, 8)
    p8_2=switch_cards_suit_alt(discard_down_cards,p8_1,13)
    p9_1=switch_cards_values(discard_down_cards,p9,12)
    p3_1=switch_cards_suit(discard_up_cards, p3, 6)
    p5_1=switch_cards_suit(discard_up_cards,p5,8)
    p7_1=switch_cards_suit(discard_up_cards,p7,9)

    p1_alt = ['                ']*len_cards
    p2_alt = ['     ___________'] * len_cards
    p3_alt = ['    /v        /'] * len_cards
    p4_alt = ['    | s        |'] * len_cards
    p5_alt = ['   /          / '] * len_cards
    p6_alt = ['  /     s    /  '] * len_cards
    p7_alt = ['  |          |  '] * len_cards
    p8_alt = [' /       s  /   '] * len_cards
    p9_alt = ['/       v /    '] * len_cards
    p10_alt =['|__________|    '] * len_cards
    p0_alt = ['[    X    ]    ']*len_cards
    p3_alt_1 = switch_cards_values(layer_down_cards, p3_alt, 5)
    p9_alt_1 = switch_cards_values(layer_down_cards, p9_alt, 8)
    p4_alt_1 = switch_cards_suit(layer_down_cards, p4_alt, 6)
    p6_alt_1 = switch_cards_suit(layer_down_cards, p6_alt, 8)
    p8_alt_1 = switch_cards_suit(layer_down_cards, p8_alt, 9)
    p0_alt_1 = count_num_user_cards(p0_alt,5)

    p1.extend(p1_alt)
    p2_1.extend(p2_alt)
    p3_1.extend(p3_alt_1)
    p4.extend(p4_alt_1)
    p5_1.extend(p5_alt)
    p6.extend(p6_alt_1)
    p7_1.extend(p7_alt)
    p8_2.extend(p8_alt_1)
    p9_1.extend(p9_alt_1)
    p10.extend(p10_alt)
    p0.extend(p0_alt_1)

    if len(cards) > 15:
        i1 = ['                    ']
        i2 = ['   ________________ ']
        i3 = ['  /Кол-во карт-L /|']
        i4_1=[' /_______________//|']
        i5_1=[' |===============|/|']
        i6_1=[' |===============|/|']
        i7 = [' |===============|/ ']
        i8 = ['    /      s  /    ']
        i9 = ['   /      v /      ']
        i10= ['  |__________|      ']
        i3_1=switch_cards_len(i3,15)
        i8_1=switch_cards_suit(trump_card_list, i8, 11)
        i9_1=switch_cards_values(trump_card_list, i9, 10)

    if len(cards) <= 15 and len(cards) > 10:
        i1 = ['                   ']
        i2 = ['                   ']
        i3_1=['  ________________ ']
        i4 = [' /Кол-во карт- L /|']
        i5_1=['/_______________//|']
        i6_1=['|===============|/|']
        i7 = ['|===============|/ ']
        i8 = ['   /       s  /    ']
        i9 = ['  /       v /      ']
        i10= [' |__________|      ']
        i4_1 = switch_cards_len(i4, 15)
        i8_1 = switch_cards_suit(trump_card_list, i8, 11)
        i9_1 = switch_cards_values(trump_card_list,i9, 10)

    if len(cards) <= 10 and len(cards) > 5:
        i1 = ['                   ']
        i2 = ['                   ']
        i3_1 = ['                   ']
        i4_1 = ['  ________________ ']
        i5 = [' /Кол-во карт- L /|']
        i6_1= ['/_______________//|']
        i7 = ['|===============|/ ']
        i8 = ['   /       s  /    ']
        i9 = ['  /       v /      ']
        i10= [' |__________|      ']
        i5_1 = switch_cards_len(i5, 15)
        i8_1 = switch_cards_suit(trump_card_list, i8, 11)
        i9_1 = switch_cards_values(trump_card_list, i9, 10)

    if len(cards) <= 5:
        i1 = ['                   ']
        i2 = ['                   ']
        i3_1 = ['                   ']
        i4_1 = ['                   ']
        i5_1 = ['  ________________ ']
        i6 = [' /Кол-во карт- L / ']
        i7 = ['/_______________/  ']
        i8 = ['   /       s  /    ']
        i9 = ['  /       v /      ']
        i10= [' |__________|      ']
        i6_1 = switch_cards_len(i6, 15)
        i8_1 = switch_cards_suit(trump_card_list, i8, 11)
        i9_1 = switch_cards_values(trump_card_list, i9, 10)

    print(battle_unification(i1)+unification_alt(p1))
    print(battle_unification(i2)+unification_alt(p2_1))
    print(battle_unification(i3_1)+unification_alt(p3_1))
    print(battle_unification(i4_1)+unification_alt(p4))
    print(battle_unification(i5_1)+unification_alt(p5_1))
    print(battle_unification(i6_1)+unification_alt(p6))
    print(battle_unification(i7)+unification_alt(p7_1))
    print(battle_unification(i8_1)+unification_alt(p8_2))
    print(battle_unification(i9_1)+unification_alt(p9_1))
    print(battle_unification(i10)+unification_alt(p10))
    if len(layer_down)>0:
        print('     Козырь:'+'        Номера:'+battle_unification(p0))
    else:
        print('     Козырь:')
    print()

############################################################################################################################################################################################################################

def first_player_turn():     #первый ход игрока в цикле(помещение выбранных карт в layer_down и их удаление в прошлом хранилище)
    global layer_down
    global user_cards
    global user_can_attack
    discard_layer_duo = []
    discard_layer_duo.extend(discard_layer_up)
    discard_layer_duo.extend(discard_layer_down)           # СДЕЛАТЬ МЕНЮ ВЫБОРА  1-сделать чото 2-сделать чото другое
    player_attack_turn_check = True
    while player_attack_turn_check:
        print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        print('Ты ходишь \n1-положить карту, 2-завершить ход, 3-пас, 4-забрать карту')
        user_text_general=input('--- ')       #номер карты
        if user_text_general == '1':
            if len(layer_down)==len(bot_cards):
                print('слишком много карт')
                sleep(1.75)
                continue
            print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
            print('выбери номер карты, которую хочешь положить')
            user_card_index=int(input('--- '))-1
            if user_card_index+1>len(user_cards) or user_card_index<0:
                print('ошибка')
                sleep(1.75)
                continue
            selected_user_card=user_cards[user_card_index]
            if len(layer_down)==0 and len(discard_layer_duo)==0:
                layer_down.append(selected_user_card)
                user_cards.remove(selected_user_card)
            else:
                card_equally=False
                layer_down_and_discard=[]
                layer_down_and_discard.extend(layer_down)
                layer_down_and_discard.extend(discard_layer_duo)
                if int(selected_user_card[0:-2])>20:
                    selected_user_card_trump=str(int(selected_user_card[0:-2])-20)+selected_user_card[-2:]
                else:
                    selected_user_card_trump=selected_user_card
                for card in layer_down_and_discard:
                    if int(card[0:-2])>20:
                        card=str(int(card[0:-2])-20)+card[-2:]
                    if selected_user_card_trump[0:-2]==card[0:-2]:
                        card_equally=True
                if card_equally==False:
                    print('ошибка')
                    sleep(2)
                    continue
                layer_down.append(selected_user_card)
                user_cards.remove(selected_user_card)
        elif user_text_general == '2':
            if len(layer_down)>0:
                player_attack_turn_check = False
            else:
                print('ошибка')
                sleep(1.75)
        elif user_text_general == '3':
            if len(discard_layer_duo)>0 and len(layer_down)==0:
                player_attack_turn_check = False
                discard_layer_down.clear()
                discard_layer_up.clear()
                user_can_attack=False
            else:
                print('ошибка')
                sleep(1.75)
        elif user_text_general == '4':
            if len(layer_down)>0:
                print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
                print('выбери карту, которую хочешь забрать (только те, которые не отбиты)')
                layer_down_card_index=int(input('--- '))-1
                selected_layer_down_card=layer_down[layer_down_card_index]
                layer_down.remove(selected_layer_down_card)
                user_cards.append(selected_layer_down_card)
            else:
                print('ошибка')
                sleep(1.75)


def bot_defense_turn(): # реагирование бота на карты в layer_down и ответ на них. все карты идут в биту при отбивании
    global bot_cards
    global layer_down
    global layer_up
    global discard_layer_down
    global discard_layer_up
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


def first_bot_turn():
    global bot_cards
    global discard_layer_down
    global discard_layer_up
    global layer_down
    print('Бот думает')
    sleep(2)
    discard_layer_duo=[]
    discard_layer_duo.extend(discard_layer_up)
    discard_layer_duo.extend(discard_layer_down)
    if len(layer_down)==len(user_cards):
        return
    if len(discard_layer_duo)==0:  #если в discard нету карт
        card=bot_cards[randint(0,len(bot_cards)-1)]
        bot_cards.remove(card)
        more_1=[]
        for bot_card in bot_cards:
            if int(bot_card[0:-2])>20:
                bot_card_trump = str(int(bot_card[0:-2])-20)+bot_card[-2:]
            else:
                bot_card_trump = bot_card
            if int(card[0:-2]) > 20:
                card_trump = str(int(card[0:-2]) - 20) + card[-2:]
            else:
                card_trump=card

            if card_trump[0] == bot_card_trump[0]:
                more_1.append(bot_card)
                bot_cards.remove(bot_card)
                continue
        if len(more_1) >= 1:
            if randint(1,4)==4:
                more_1.append(card)
                layer_down.extend(more_1)
            else:
                layer_down.append(card)
        else:
            layer_down.append(card)
    else:                                                 #если в discard есть карты
        discard_layer_duo_with_trump_card=[]
        for card in discard_layer_duo:                   #перевод козырных карт discard
            if int(card[0:-2]) < 20:
                discard_layer_duo_with_trump_card.append(card)
            else:
                discard_layer_duo_with_trump_card.append(str(int(card[0:-2]) - 20)+card[-2:])
        bot_cards_can_attack=set([])
        for discard_card in discard_layer_duo_with_trump_card:
            for bot_card in bot_cards:
                if int(bot_card[0:-2]) > 20:
                    bot_card_trump = str(int(bot_card[0:-2]) - 20) + bot_card[-2:]
                else:
                    bot_card_trump = bot_card

                if discard_card[0:-2]==bot_card_trump[0:-2]:
                    bot_cards_can_attack.add(bot_card)
        if len(bot_cards_can_attack)==0:
            print('ты отбился')
        else:
            bot_attack=[]
            bot_cards_can_attack_list=list(bot_cards_can_attack)
            shuffle(bot_cards_can_attack_list)
            bot_cards_can_attack_list_trump=[]

            for card in bot_cards_can_attack_list:  # перевод козырных карт discard
                if int(card[0:-2]) < 20:
                    bot_cards_can_attack_list_trump.append(card)
                else:
                    bot_cards_can_attack_list_trump.append(str(int(card[0:-2]) - 20) + card[-2:])

            for card in bot_cards_can_attack_list[1:]:
                if int(card[0:-2])>20:
                    card_tramp=str(int(card[0:-2])-20)+card[-2:]
                else:
                    card_tramp=card

                if card_tramp[0:-2]==bot_cards_can_attack_list_trump[0][0:-2]:
                    bot_attack.append(card)
                    bot_cards.remove(card)
            bot_attack.append(bot_cards_can_attack_list[0])
            bot_cards.remove(bot_cards_can_attack_list[0])
            layer_down.extend(bot_attack)


def player_defense_turn():
    global user_cards
    global layer_down
    global discard_layer_down
    global discard_layer_up
    player_defense_turn_check=True
    while player_defense_turn_check:
        print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        print('Ты отбиваешься \n1-положить карту, 2-завершить ход, 3-взять')
        user_text=input('--- ')
        if user_text == '1':
            if len(layer_down)==0:
                print('ходить некуда')
                sleep(1.75)
                continue
            while True:
                print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
                print('напиши номер СВОЕЙ карты, которую хочешь положить')
                user_card_index=int(input('--- '))-1
                print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
                print('напиши номер карты, которую ты будешь отбивать (уже отбитые карты не считаются!!!!!!!!!)')
                layer_down_card_index=int(input('--- '))-1
                if int(user_cards[user_card_index][0:-2])>int(layer_down[layer_down_card_index][0:-2]) and user_cards[user_card_index][-1]==layer_down[layer_down_card_index][-1] or int(user_cards[user_card_index][0:-2])-10>int(layer_down[layer_down_card_index][0:-2]):
                    discard_layer_up.append(user_cards[user_card_index])
                    discard_layer_down.append(layer_down[layer_down_card_index])
                    user_cards.remove(user_cards[user_card_index])
                    layer_down.remove(layer_down[layer_down_card_index])
                    break
                else:
                    print('ошибка')
                    sleep(1.75)
                    break
        elif user_text == '2':
            if len(layer_down)==0:
                player_defense_turn_check=False
            else:
                print('ошибка')
                sleep(1.75)
        elif user_text == '3':
            user_cards.extend(layer_down)
            layer_down.clear()
            user_cards.extend(discard_layer_up)
            discard_layer_up.clear()
            user_cards.extend(discard_layer_down)
            discard_layer_down.clear()
            player_defense_turn_check=False


def cycle_attack_check(discard_layer_up,discard_layer_down,user_card):    #если каждое значение карты cards есть в discard_layer_duo то True, иначе False
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


def giveaway(turn):
    global cards
    global bot_cards
    global user_cards
    global trump_card_allowed
    what_need_user_card=6-len(user_cards)
    what_need_bot_card=6-len(bot_cards)
    if what_need_user_card<0:
        what_need_user_card=0
    if what_need_bot_card<0:
        what_need_bot_card=0
    if turn=='бот':
        bot_cards.extend(cards[0:what_need_bot_card])
        del cards[0:what_need_bot_card]
        user_cards.extend(cards[0:what_need_user_card])
        del cards[0:what_need_user_card]
    elif turn=='игрок':
        user_cards.extend(cards[0:what_need_user_card])
        del cards[0:what_need_user_card]
        bot_cards.extend(cards[0:what_need_bot_card])
        del cards[0:what_need_bot_card]
    sleep(2)
    print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
    if len(cards)!=0:
        print('роздача карт')
    sleep(2)


def win():
    if len(cards)==0:
        if len(bot_cards)==0 and len(user_cards)!=0:
            print('бот выйграл')
            return True
        elif len(bot_cards)!=0 and len(user_cards)==0:
            print('ТЫ ВВВЫЙГРАЛ!!!')
            return True


layer_up=[]
layer_down=[]
discard_layer_down=[]
discard_layer_up=[]
cards_deck=['1:Ч','2:Ч','3:Ч','4:Ч','5:Ч','6:Ч','7:Ч','8:Ч','9:Ч',
       '1:Б','2:Б','3:Б','4:Б','5:Б','6:Б','7:Б','8:Б','9:Б',
       '1:П','2:П','3:П','4:П','5:П','6:П','7:П','8:П','9:П',
       '1:К','2:К','3:К','4:К','5:К','6:К','7:К','8:К','9:К',]
cards = []
shuffle(cards_deck)

trump_card_allowed=True
trump_card=cards_deck[0]       #задается козырь
del cards_deck[0]
trump_card_list=[]
trump_card_list.append(trump_card)

#trump_card='6:К'

for card in cards_deck:          # перебор карт и изменение числа козырей на n+20
    if card[-1] == trump_card[-1]:
        num_card = int(card[0:-2]) + 20
        cards.append(str(num_card) + card[-2:])
    else:
        cards.append(card)

trump_card=str(int(trump_card[0:-2])+20)+trump_card[-2:] # сам козырь тоже изменяется на n+20
cards.append(trump_card)

user_cards=cards[0:6]   # берется 6 начальных карт из колоды для игрока
del cards[0:6]

bot_cards=cards[0:6]    # берется 6 начальных карт из колоды для бота
del cards[0:6]

#bot_cards=['23:К','23:П','23:Ч','3:Б','2:Б']
#user_cards=['1:П','1:Ч','1:Б','2:Ч','22:К','3:П','1:Ч','1:Б','2:Ч','22:К','3:П']
#layer_up=[]
#layer_down=['3:П','1:П','1:Ч','1:Б','2:Ч','22:К','3:П','1:П','1:Ч','1:Б','2:Ч','22:К','3:П']
#discard_layer_down=['23:К','9:Б']
#discard_layer_up=['5:П',"23:К"]

while True:                            #цикл ходов
    if win()==True:
        break
    bot_cards_len_before=len(bot_cards)
    print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
    first_player_turn()
    print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
    bot_defense_turn()
    print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
    bot_cards_len_after = len(bot_cards)
    if bot_cards_len_before>=bot_cards_len_after:
        user_can_attack=cycle_attack_check(discard_layer_up,discard_layer_down,user_cards)
    elif len(user_cards)==0:
        user_can_attack = False
    else:
        user_can_attack=True
        giveaway('игрок')
    if user_can_attack:
        print('ты можешь сделать еще один ход')
        sleep(2) # 2
    if win()==True:
        break
    while user_can_attack:
        if win() == True:
            break
        bot_cards_len_before = len(bot_cards)
        print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        first_player_turn()
        print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
        bot_defense_turn()
        print_all_card_tab(bot_cards,'Карты противника:',user_cards,'Твои карты:',layer_down,discard_layer_up,discard_layer_down)
        bot_cards_len_after = len(bot_cards)
        if bot_cards_len_before>=bot_cards_len_after:
            user_can_attack=cycle_attack_check(discard_layer_up, discard_layer_down, user_cards)

        elif len(user_cards) == 0:
            user_can_attack = False
        else:
            user_can_attack = True
            giveaway('игрок')
        if user_can_attack :
            print('Ты можешь сделать еще один ход')
            sleep(2)  # 2
    discard_layer_down.clear()
    discard_layer_up.clear()
    if win()==True:
        break
    giveaway('игрок')
    user_cards_len_before = len(user_cards)
    print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
    first_bot_turn()
    print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
    player_defense_turn()
    print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
    user_cards_len_after = len(user_cards)
    if user_cards_len_before>user_cards_len_after:
        bot_can_attack=cycle_attack_check(discard_layer_up,discard_layer_down,bot_cards)

    elif len(bot_cards)==0:
        bot_can_attack = False
    else:
        bot_can_attack=True
        giveaway('бот')
    if win()==True:
        break
    while bot_can_attack:
        if win() == True:
            break
        user_cards_len_before = len(user_cards)
        print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
        first_bot_turn()
        print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
        player_defense_turn()
        print_all_card_tab(bot_cards, 'Карты противника:', user_cards, 'Твои карты:',layer_down, discard_layer_up, discard_layer_down)
        user_cards_len_after = len(user_cards)
        if user_cards_len_before > user_cards_len_after:
            bot_can_attack = cycle_attack_check(discard_layer_up, discard_layer_down, bot_cards)

        elif len(bot_cards) == 0:
            bot_can_attack = False
        else:
            bot_can_attack = True
            giveaway('бот')
    if win()==True:
        break
    discard_layer_down.clear()
    discard_layer_up.clear()
    giveaway('бот')
sleep(10)
# :)