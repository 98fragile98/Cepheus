import random
from tkinter import *

#Para Sistemi

root = Tk()
root.title('Blackjack')
root.geometry('250x270')
root.resizable(0,0)
root.attributes('-topmost', True)

cardList = ["As", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Kız", "Papaz", "Oğlan"]

def carddraw():
    if len(cardList) != 0:
        card = random.choice(cardList)
        print(card)
        cardList.remove(card)
    else:
        print("Kart kalmadı!")
def cardcall():

    

card_value_lbl = Label(root, text='Value of Cards')
card_value_lbl.grid(row=1, column=0, columnspan=3, sticky="EW")
carddraw_btn= Button(root, text='Draw', command=carddraw)
carddraw_btn.grid(row=2, column=0, columnspan=3, pady=10, padx=10, ipadx=100,sticky="NSEW")
cardcall_btn= Button(root, text='Call', command=cardcall)
cardcall_btn.grid(row=2, column=0, columnspan=3, pady=10, padx=10, ipadx=100,sticky="NSEW")

# =============================================================================
# reqcard = 0
# while True:
#     reqcard = input("Kart çekmek istiyormusunuz ? e/h\n")
#     if reqcard == "e":
#         carddraw()
#     elif reqcard == "h":
#         break
#     elif reqcard != "e" or "h":
#         print("Lütfen geçerli bir cevap veriniz!")
# =============================================================================

root.mainloop()
