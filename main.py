import random
b = random.randint(0,100)
c = 0
while True:
     a = int(input(f"{c}/{10} num:"))
     if b < a:
         print("меньше")
     else:
         c = c + 1
     if b > a:
         print("больше")
     else:
         c = c + 1
     if b==a:
         print("победил")
         break
     if c == 10:
         print(f"{c}/{10} проиграл")
         break