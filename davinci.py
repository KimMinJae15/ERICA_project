# OSS project 2019057956 "KimMinJae"
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
	print("===================")
	print("	당신 차례입니다. 타일을 뽑으세요!")
	p2, black, white = p2_turn(p2,black,white)
	p2.sort()

def joker:
    jo = random.randint(1,13)
    
    if jo  = 1:
        b = random.randint(1,2)
            if(b = 1):
                # 검은색 조커 추가

            else:
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
		else:
			card, black = black[0], black[1:]
			p1.append(card)

   else:
		if white = []:
			if black = []:
				pass

			else:
				card, black = black[0], black[1:]
				p1.append(card)
    	else:
			card, white = white[0], white[1:]
			p1.append(card)
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
				#보여주기?



def show_p1:


def p2_turn
