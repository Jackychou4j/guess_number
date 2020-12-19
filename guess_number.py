import random
number = random.randint(0,100)
print(number)
guess_times = 0
while True:
    guess = input("請輸入數字:")
    guess = int(guess)
    guess_times =  guess_times +1
    if guess == number:
        print("恭喜，你猜對了")
        print("你總共猜了",guess_times,"次")
        break
    elif guess < number:
        print("猜錯了，在大一點")
    elif guess > number:
        print("猜錯了，在小一點")
#檢討：讓使用者重複輸入，你的input就要放在while迴圈，不然出不去。
#檢討二：不能寫兩個while分別判斷，因為輸入的input還是在外面，這樣會回不去。(第22行)
#===================================================測試二(無法)
# import random
# number = random.randint(0,100)
# guess = input("請輸入數字:")
# guess = int(guess)
# print(number)
# guess_times = 0
# while guess == number:
#     guess_times =  guess_times +1
#     print("恭喜，你猜對了")
#     print("你總共猜了",guess_times,"次")
#     break
# while guess != number:
#     if guess < number:
#         print("猜錯了，在大一點")
#     elif guess > number:
#         print("猜錯了，在小一點")

