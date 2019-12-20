# OSS project 2019057956` "KimMinJae"
# Davinci code
##################################
import random
def dvc_code():
    print("=========================")
    print("Welcome to 'Da Vinci Code'.")
    print("========================")

    black = ['1검','2검','3검','4검','5검','6검','7검','8검','9검','A검','B검','C검']
    white = ['1흰','2흰','3흰','4흰','5흰','6흰','7흰','8흰','9흰','A흰','B흰','C흰']
    
    b_J = [조커]
    w_J = [조커]
    
    
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

    card, white = get_card(white)
    p1.append(card)
    card, white = get_card(white)
    p1.append(card)
    card, white = get_card(white)
    p2.append(card)

    p1.sort()
    p2.sort()
	p1_new = [] # 새로운
	p2_new = []
	p1_show = []
	p2_show = [] # 보여줄 카드 리스트	
	
	show_p1(p1,p1_show)
	show_p2(p2)

	while True:
		try:
			print("===================")
			print("	당신 차례입니다. 타일을 뽑으세요!")
			p2, black, white,p2_new = p2_turn(p2,black,white,p2_new)
			p2.sort()
			
			print()
			show_p2(p2)
			show_p1(p1,p1_show)
			print("공개된 내 타일 : ", end = '')
			for i in p2_show:
			print(i+' ', end = '')
			print('\n')
			#공개된 내 타일
			
			p1_show, p2_show = p2_check(p1,p2_new,p1_show,p2_show)

			show_p2(p2)
			show_p1(p1,p1_show)
			p2_show.sort()
			print("공개된 내 타일 : ", end = '')
			for i in p2_show:
				print(i + ' ', end = '')
			print()
			#공개된 내 타일
			
			if len(p1) == len(p1_show): raise PlayerWin # player가 이긴 경우 예외 처리 	

			####p1 턴

			print("==================")
			print("	computer가 타일 뽑는 중 ")
			time.sleep(1)
                        print('...', end = ' ')
                        time.sleep(1)
                        print()
                        p1, black, white, p1_new = p1_turn(p1,black,white,p1_new) #p1이 카드 뽑기(검정, 흰색 중 랜덤)
                        p1.sort()

                        show_p2(p2)
                        show_p1(p1,p1_show)
                        print("공개된 내 타일 : ", end = '')
                        #
						for i in p2_show:
							print(i+' ', end = '')
						print('\n')

                        print(" computer가 당신의 타일을 맞추는 중")
                        time.sleep(1)
                        print('...', end = ' ')
                        time.sleep(1)
                        print()
                        p1_show, p2_show = p1_check(p2,p2_show,p1_show,p1_new)

                        show_p2(p2)
                        show_p1(p1,p1_show)
                        p2_show.sort()
                        print("공개된 내 타일 : ", end = '')
                        for i in p2_show:
							print(i + ' ', end = '')

                        print()
                        
                        if len(p2) == len(p2_show): raise ComputerWin #Computer가 이긴 경우 예외처리 
                        

			except PlayerWin:
                            print("")
                            print(" 이겼습니다! 축하드립니다!")
                            more_game
                            break
			except ComputerWin:
                            print("")
                            print(" 아쉽게도 졌네요 ㅠㅠㅠ")
                            more_game()
                            break

			
#def joker:
#   jo = random.randint(1,13)
    
#   if jo  = 1:
#       b = random.randint(1,2)
#           if(b = 1):
                # 검은색 조커 추가

#           else:
                # 흰색 조커 추가

        #조커 카드 추가 

    #13분의 1 확률로 조커 가져오기
    #진행중

#섞은 카드 첫번째 인덱스 가져오기, 나머지 반환
def get_card(tile):
    return (tile[0], tile[1:])


#뽑기
def p1_turn(p1,black,white):
    a = random.randint(1,2)
    if a = 1:
    	if black = []:
	    
	    if white = []:
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
	if white = []:
	    if black = []:
		pass

	    else:
		card, black = black[0], black[1:]
		p1.append(card)
    		p1_new.append(card)

	else:
	    card, white = white[0], white[1:]
	    p1.append(card)
	    p1_new.append(card) # p1이 뽑은 카드들을 모두 새 리스트에

    return (p1,black,white)



#컴퓨터가 맞추기
def p1_check:
	black_copy = ['1검','2검','3검','4검','5검','6검','7검','8검','9검','A검','B검','C검']

 	white_copy = ['1흰','2흰','3흰','4흰','5흰','6흰','7흰','8흰','9흰','A흰','B흰','C흰']
	#p1 길이 랜덤으로 받고 random(1,p1길이) 한 다음에 만약 그 카드가 검은색이면 black이랑 p			1카드중 하나 뽑고
	#그 카드가 흰색이면 white랑 p2카드중에서 하나 뽑고 
	c = 0
	for i in range(len(p2)-1):
		a = random.randint(1, len(p2))
		if "검" in p2[a-1]:
			b = black_copy[random.randint(0,len(black_copy)-1]
			if(p2[a-1] == b):
			    print("")
                            print()
                            p2_show.append(b)
                            c+=1
                            break
                        else:
                            continue
                elif "흰" in p2[a-1]:
                    b = white_copy[random.randint(0, len(white_copy)-1)
                    if (p2[a-1] == b):
                        print("컴퓨터가 당신의 타일을 맞췄습니다!")
                        print()
                        p2_show.append(b)
                        c+=1
                        break
                    else:
                        continue

                        #보여주기?


    if c == 0:
        print("컴퓨터가 당신의 타일을 맞추지 못했습니다.")
        print()
        p1_show.append(p1_new[len(p1_new)-1])
    return (p1_show,p2_show)

def show_p1:


def p2_turn(p2,black,white,p2_new):
	if black = []:
		if white = []:
			print("더 이상 가져올 타일이 없습니다.\n추리를 진행하세요.")
		
		else:
			print("검은색 타일이 없습니다. \n흰색 타일을 가져옵니다.")
			card, white = white[0], white[1:]
			p2.append(card)
			p2_new.append(card)
	elif white == []:
		print("흰색 타일이 없습니다.\n검은색 타일을 가져옵니다.")
		card, black = black[0], black[1:]
		p2.append(card)
		pew_new.append(card)

	else:

            color = input("어떤 색의 타일을 가져오시겠습니까? b/w: ")

            while not (color == 'b' or color == 'w'):
                print("타일의 색을 b 혹은 w로 입력해주세요. ")
                color = input("어떤 색의 타일을 가젼오시겠습니까? b/w: ")

            if color == "b":
                color, black = black[0], black[1:]
                p2.append(card)
                #가져온 카드 새로운 리스트에 넣기
                p2_new.append(card)

            else:
		# 둘다 잔여 카드가 남았을때

            card, white = white[0], white[1:]
            p2.append(card)
            p2_new.append(card)
    return (p2,black,white,p2_new)

def show_p2(p2):
    print("내 타일:", end = '')
    for i in p2:
        print(i+' ', end = '')
    

def more_game(): 
    a = input("새 게임을 진행 하시겠습니까? y/n: ")
    while not (a == 'y' or a == 'n'):
        a = input("새 게임을 진행하시겠습니까? y/n")
    if a == 'y':
        dvc_code()

    else:
        print("GoodBye!")
        time.sleep(2)

        

