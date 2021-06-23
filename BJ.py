import random

cardList = ["As", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Kız", "Papaz", "Oğlan"]


def carddraw():
    if len(cardList) != 0:
        card = random.choice(cardList)
        print(card)
        cardList.remove(card)
    else:
        print("Kart kalmadı!")


reqcard = 0
while True:
    reqcard = input("Kart çekmek istiyormusunuz ? e/h\n")
    if reqcard == "e":
        carddraw()
    elif reqcard == "h":
        break
    elif reqcard != "e" or "h":
        print("Lütfen geçerli bir cevap veriniz!")
