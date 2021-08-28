# 產生一個隨機整數1~100（不要印出來
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了！"
# 猜錯的話要告述他比答案大/小
import random
number = random.randint(1, 100)
time = 0
while True:
	time += 1 # 等於 time = time +1
	question = input("請猜數字(1~100)：")
	question = int(question)
	if question == number:
		print("你猜對了！")
		print("這是你猜的第", time, "次")	
		break
	elif question > number:
		print("數字太大了，再試一次！")
	elif question < number:
		print("數字太小了，再試一次！")
	print("這是你猜的第", time, "次")