import random,time
pokers = []
money = 1000
def poker():
	global pokers
	print('洗牌中。。。')
	for i in range(1,53):
		pokers.append(i)

def d_cards():
	num = random.choice(pokers)
	pokers.remove(num)
	return num

def points(num_list):
	result = 0
	for i in num_list:
		if i%13 == 11 or i%13 == 12 or i%13 == 0:
			result += 10
		elif i%13 == 1 and result <= 10:
			result += 11
		else:
			result += i%13
	return result

def card_color(num):
	color_list = ['K','J','Q']
	if num % 13 > 10 or num % 13 ==0:
		if 10 < num < 14:
			return '方块' + color_list[num%13%10]
		elif 23 < num < 27:
			return '梅花' + color_list[num%13%10]
		elif 36 < num < 40:
			return '红桃' + color_list[num%13%10]
		elif 49 < num < 53:
			return '黑桃' + color_list[num%13%10]
	else:
		if num < 13:
			return '方块' + str(num)
		elif 13 < num < 26:
			return '梅花' + str(num%13)
		elif 26 < num < 39:
			return '红桃' + str(num%13)
		else:
			return '黑桃' + str(num%13)
			
def ai():
	global c_num
	num = points(c_cards)
	if num <= 17:
		c_cards.append(d_cards())
		ai()
	elif 17 < num < 21:
	 	choices = random.choice((0,1))
	 	if choices:
	 	 	c_cards.append(d_cards())
	 	 	ai()
	 	else:
	 	 	c_num = num
	else:
	 	c_num = num
	 	
def wol():
	if points(your_cards) <= 21:
		print('是否要牌？ Y/N')
		res = input('>>>>')
		if res == 'y' or res == 'Y':
			card = d_cards()
			your_cards.append(card)
			print('您摸到的牌为' + card_color(card))
			print('你现在有%d张牌,点数为%d点' % (len(your_cards),points(your_cards)))
			wol()
		else:
			print('电脑摸牌中。。。')
			time.sleep(1)
			ai()
			your_num = points(your_cards)
			if your_num == c_num:
				print('打成平手哟！')
			elif c_num > 21:
				print('电脑爆炸了！点数为%d' % points(c_cards))
			elif your_num > c_num:
				print('你赢了!电脑的点数为%d(⌯¤̴̶̷̀ω¤̴̶̷́)✧' % points(c_cards))
			elif your_num < c_num:
				print('你输了！电脑的点数为%d,(இωஇ )' % points(c_cards))
	else:
		print('boom!你的点数为%d' % points(your_cards))
	
	 		
def main():
	global your_cards,c_cards
	if len(pokers) < 10:
		poker()
		main()
	else:
		print ('**********欢迎来到21点**********')
		your_cards = []
		c_cards = []
		for i in range(2):
			card = d_cards()
			print('您摸到的牌为' + card_color(card))
			your_cards.append(card)
			c_cards.append(d_cards())
			print('你现在有%d张牌,点数为%d点' % (len(your_cards),points(your_cards)))
		wol()
			
while 1:
	main()