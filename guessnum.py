import random
num_start = input('請決定隨機範圍開始值: ')
num_end = input('請決定隨機數字結束值: ')
num_start = int(num_start)
num_end = int(num_end)

r = random.randint(num_start, num_end)
count = 0  #如果寫在while裡面會變成歸零
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大了!再猜唷!')
	elif num < r:
		print('比答案小了! 再猜猜!')
	print('這是你猜的第', count, '次')