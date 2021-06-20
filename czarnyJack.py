import random
import time

poklad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
poklad *= 4

ladowanie = list("LOADING")
for i in range(7):
    time.sleep(.4)
    print(ladowanie[i])

print("\nС подключением, Username.\nСыграем с тобой в игру, ставка твоя жизнь")
time.sleep(4)
print("\nШутка. Сыграем в блэкджек со шлюхами.\nС меня блэкджек, итак - поехали")
time.sleep(3)
nic = input("\nИграем? Нажми что угодно. Мне плевать что  ")
print("\n", nic, "это не самый оригинальный выбор в твоей жизни")

renka = 0
while renka < 21:
    decyzja = input("\nБерешь карту? Отвечай только \"+\" или \"-\" ")
    if decyzja == "+":
        renka += random.choice(poklad)
        print(renka)
    if decyzja == "-":
        print("\nНу и проваливай отсюда, значит")
        break
    if decyzja != "+" and decyzja != "-":
        print("\nТы немец, что ли?\nСказано же, только \"+\" или \"-\"")
if renka == 21:
    print("\nТы победил.\nХотя твоя заслуга невелика")
if renka == 20:
    print("\nОтличный результат для труса.\nМолодец")
if renka >= 22:
    print("\nТы все просрал.\nТеперь проваливай из казино, король голожопый")
print("\nТвой результат", renka)