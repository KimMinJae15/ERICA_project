# OSS project 2019057956` "KimMinJae"
# Davinci code
##################################

import random

import time

class ComputerWin(Exception): pass

class PlayerWin(Exception): pass

def manual():
	print("다빈치 코드에 오신걸 환영합니다.")
	print()
	print("다빈치 코드는 내가 가지고 있는 타일과 상대의 공개된 타일을 보고")
	print("상대방의 공개되지 않은 타일을 유추하는 보드게임입니다. ")
	print()
	print("타일은 왼쪽부터 오름차순으로 정렬되어 있습니다.")
	print()
	print("검정색 타일과 흰색 타일이 존재하며 같은 숫자를 가질수 있습니다.")
	print()
	print("예를 들어 검정색타일1과 흰색 타일1을 가지고 있다면, 검정색 타일이 왼쪽에 오게 됩니다. ")
	print()
	print("상대방의 타일을 맞추면 한번 더 맞출수 있는 기회가 주어집니다.")
	print("그럼 행운을 빕니다. Good Luck!")
	print()
	enter = print("Press Enter to start")
	dvc_code()

def dvc_code():
	
    print("===========================")

    print("Welcome to 'Da Vinci Code'.")

    print("===========================")
    choose = input("다빈치 코드의 룰을 아십니까? 규칙을 보려면 1번을, 시작하려면 엔터를 눌러주세요.")
    if choose == '1':
        manual()
    
    print("게임이 시작되었습니다!")
    print()
    black = ['1검', '2검', '3검', '4검', '5검', '6검', '7검', '8검', '9검', 'A검', 'B검', 'C검']

    white = ['1흰', '2흰', '3흰', '4흰', '5흰', '6흰', '7흰', '8흰', '9흰', 'A흰', 'B흰', 'C흰']

    random.shuffle(black)

    random.shuffle(white)



    p1, p2 = [], []



    card, black = get_card(black)

    p1.append(card)

    card, black = get_card(black)

    p2.append(card)

    card, black = get_card(black)

    p1.append(card)

    card, black = get_card(black)

    p2.append(card)



    card, white = get_card(white)

    p1.append(card)

    card, white = get_card(white)

    p2.append(card)

    card, white = get_card(white)

    p1.append(card)

    card, white = get_card(white)

    p2.append(card)



    p1.sort()

    p2.sort()



    p1_new = []

    p2_new = []

    p1_show = []

    p2_show = []



    show_p1(p1,p1_show)

    show_p2(p2)



    while True:

        try:



            ######## p2 턴

            print("=====================")

            print("타일을 뽑으세요.")

            p2, black, white, p2_new = p2_turn(p2,black,white,p2_new) # p2가 카드 뽑기

            p2.sort()



            print()

            show_p2(p2) # 내 카드 출력

            show_p1(p1,p1_show) # 상대 카드 출력

            print("공개된 내 타일 : ", end='')

            for i in p2_show:

                print(i + ' ', end='')

            print('\n')



            p1_show, p2_show = p2_check(p1,p2_new,p1_show,p2_show) # p2가 p1의 카드 맞추기



            show_p2(p2)

            show_p1(p1,p1_show)

            p2_show.sort()

            print("공개된 내 타일 : ", end='')

            for i in p2_show:

                print(i + ' ', end='')

            print()



            if len(p1) == len(p1_show): raise PlayerWin # player가 이긴 경우 예외 처리

            ######## p1 턴

            print("=====================")

            print("Computer가 타일 뽑는 중 ")

            time.sleep(1)

            print('. . . ', end=' ')

            time.sleep(1)

            print()

            p1, black, white, p1_new = p1_turn(p1,black,white,p1_new) # p1이 카드 뽑기 (검정, 흰색 中 랜덤)

            p1.sort()



            show_p2(p2)

            show_p1(p1,p1_show)

            print("공개된 내 타일 : ", end = '')

            for i in p2_show:

                print(i+' ', end = '')

            print('\n')



            print("Computer가 당신의 타일을 맞추는 중 ")

            time.sleep(1)

            print('. . . ', end = ' ')

            time.sleep(1)

            print()

            p1_show, p2_show = p1_check(p2,p2_show,p1_show,p1_new)



            show_p2(p2)

            show_p1(p1,p1_show)

            p2_show.sort()

            print("공개된 내 타일 : ", end='')

            for i in p2_show:

                print(i + ' ', end='')

            print()



            if len(p2) == len(p2_show): raise ComputerWin # computer가 이긴 경우 예외 처리



        except PlayerWin:

            print("=====================")

            print("이겼습니다! 축하드립니다!")

            more_game()

            break

        except ComputerWin:

            print("=====================")

            print("아쉽게도 졌네요 ㅠㅠㅠ")

            more_game()

            break



def get_card(deck):

    return (deck[0], deck[1:])



def p1_turn(p1,black,white,p1_new):

    a = random.randint(1,2)

    if a == 1:

        if black == []:

            if white == []:

                pass

            else:

                card, white = white[0], white[1:]

                p1.append(card)

                p1_new.append(card)

        else:

            card, black = black[0], black[1:]

            p1.append(card)

            p1_new.append(card)

    else:

        if white == []:

            if black == []:

                pass

            else:

                card, black = black[0], black[1:]

                p1.append(card)

                p1_new.append(card)

        else:

            card, white = white[0], white[1:]

            p1.append(card)

            p1_new.append(card)

    return (p1,black,white,p1_new)





def p1_check(p2,p2_show,p1_show,p1_new):

    black_copy = ['1검', '2검', '3검', '4검', '5검', '6검', '7검', '8검', '9검', 'A검', 'B검', 'C검']

    white_copy = ['1흰', '2흰', '3흰', '4흰', '5흰', '6흰', '7흰', '8흰', '9흰', 'A흰', 'B흰', 'C흰']
    ran = random.randrange(1,2)
# p1 길이 랜덤으로 받고 random(1,p1길이) 한다음에 만약 그 카드가 검은색이면 black이랑 p1 카드중 에서 하나 뽑고

    # 그 카드가 흰색이면 white랑 p2카드중에서 하나 뽑고

    c = 0

    for i in range(len(p2)-1):

        a = random.randint(1, len(p2))
		
        if "검" in p2[a - 1]:

            b = black_copy[random.randint(0, len(black_copy) - 1)]
            b1 = black_copy[random.randint(0,len(black_copy) - 1)]
            if (p2[a-1] == b):

                print("컴퓨터가 당신의 타일을 맞췄습니다!")
				
				
                print()

                p2_show.append(b)

                # 내 카드는 까지는게 보일 필요가 없지

                c += 1
                
                break

            elif (p2[a-1] == b1):
                print("컴퓨터가 당신의 타일을 맞췄습니다!")
                print()
                p2_show.append(b1)
                c+=1

           
            else:
                continue

        elif "흰" in p2[a - 1]:

            b = white_copy[random.randint(0, len(white_copy) - 1)]
            b1 = white_copy[random.randint(0, len(white_copy) - 1)]
            if (p2[a-1] == b):

                print("컴퓨터가 당신의 타일을 맞췄습니다!")
				
                print()

                p2_show.append(b)
                c += 1
                break
            elif (p2[a-1] == b1):
                  print("컴퓨터가 당신의 타일을 맞췄습니다.!")
                  print()
                  p2_show.append(b1)
                  c+=1
                  break
            else:

                  continue

    if c == 0:

        print("컴퓨터가 당신의 타일을 맞추지 못했습니다.")

        print()

        p1_show.append(p1_new[len(p1_new) - 1])

    return (p1_show,p2_show)



def show_p1(p1,p1_show):

    cnt = 0

    i = 0

    p1_copy = p1[:]



    while (i != len(p1)):  # p1의 위치는 그대로 이니까..

        p1_copy[i] = '□'  # p1의 리스트의 길이 만큼 ㅁ 추가 -> 추가될때 문제

        i += 1



    for s in range(len(p1)):

        if '검' in p1[s]:

            p1_copy[s] = '■'



    for i in p1:

        for j in p1_show:

            if (i == j):

                p1_copy[cnt] = j

        cnt += 1



    print("상대의 타일    :", end = '')

    for j in p1_copy:

        print(j+'  ', end = '')

    print()



def p2_turn(p2,black,white,p2_new):

    # 카드 가져오고

    if black == []:

        if white == []:

            print("더 이상 가져올 타일이 없습니다.\n추리를 진행하십시오.")

        else:

            print("검은색 타일이 없습니다.\n흰색 타일을 가져옵니다.")

            card, white = white[0], white[1:]

            p2.append(card)

            p2_new.append(card)

    elif white == []:

        print("흰색 타일이 없습니다.\n검은색 타일을 가져옵니다.")

        card, black = black[0], black[1:]

        p2.append(card)

        p2_new.append(card)

    else:



        color = input("어떤 색의 타일을 가져오시겠습니까? b/w : ")

        while not (color == 'b' or color == 'w'):

            print("타일의 색을 b 혹은 w로 입력해 주세요.")

            color = input("어떤 색의 타일을 가져오시겠습니까? b/w : ")

        if color == "b":

            card, black = black[0], black[1:]

            p2.append(card)

            # 가져온 카드 새로운 리스트에 넣기

            p2_new.append(card)

        else:

            card, white = white[0], white[1:]

            p2.append(card)

            p2_new.append(card)

    return (p2,black,white,p2_new)





def p2_check(p1,p2_new,p1_show,p2_show):

    while True:

        try:

            pos1 = int(input("  위치: "))

            while not (pos1 <= len(p1) and pos1 >= 1):

                print("타일의 위치 번호를 제대로 입력해 주세요.")

                pos1 = int(input("위치: "))



            if '검' in p1[pos1-1]:

                card1_color = '검'

            else:

                card1_color = '흰'



            card1_num = input("예상되는 타일의 번호 또는 알파벳 : ")

            while not (card1_num == '1' or card1_num == '2' or card1_num == '3' or card1_num == '4' or card1_num == '5' or card1_num == '6' or card1_num == '7' or card1_num == '8' or card1_num == '9' or card1_num == 'A' or card1_num == 'B' or card1_num == 'C'):

                print("제대로 입력해 주세요.")

                card1_num = input("예상되는 타일의 번호 또는 알파벳: ")

            card1 = card1_num + card1_color

            if (p1[pos1-1] == card1):

                print("맞췄습니다!")

                # 상대 카드 까기

                # 깐 카드 리스트에 넣기 -> show_p1에 넣기

                p1_show.append(card1)

                show_p1(p1,p1_show)

                trial = input("한번 더 맞추시겠습니까? y/n : ")

                while not (trial == 'y' or trial == 'n'):

                    trial = input("한번 더 맞추시겠습니까? y/n :")

                if (trial == "y"):

                    continue

                else:

                    print("턴을 넘기겠습니다.")

                    break

            else:

                print("틀렸습니다.")

                print("Computer에게",p2_new[-1],"이(가) 공개됩니다.")

                print()

                p2_show.append(p2_new[-1])

                # new[]에서 가장 최근 카드 까기

                break

        except ValueError:

            print("범위 내의 숫자를 알맞게 입력해 주세요.")

            continue



    return (p1_show,p2_show)



def show_p2(p2):

    print("내 타일:         ", end = '')

    for i in p2:

        print(i+' ', end = '')

    print()





def more_game(): # 게임을 더 할 건지 여부를 묻는다

    a = input("새 게임을 진행하시겠습니까? y/n : ")

    while not (a == 'y' or a == 'n'):

        a = input("새 게임을 진행하시겠습니까? y/n : ")

    if a == 'y':

        dvc_code()

    else:

        print("Good Bye!")

        time.sleep(2)



dvc_code()


