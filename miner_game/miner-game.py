from tkinter import *

balance = 0
speed = 1
click = 2
priceclick = 1
pricespeed = 1

sc = Tk()
sc['bg'] = '#1f1f1f'
sc.geometry('500x800')
sc.resizable(height = True, width = True)
f1 = Frame(sc, bg = '#1f1f1f', width = 500, height = 800)
f2 = Frame(sc, bg = '#1f1f1f', width = 500, height = 800)
cv = Canvas(sc, width = 500, height = 800, bg = '#1f1f1f')
cv2 = Canvas(sc, width = 500, height = 800, bg = '#1f1f1f')
showbal = Label(cv, text = balance, bg = '#1f1f1f', fg = 'white', font = 30)
showspeed = Label(cv, text = f'{speed}\nper second', fg = 'white', bg = '#1f1f1f')
showclick = Label(cv, text = f'{click}\nper click', fg = 'white', bg = '#1f1f1f')
showpriceclick = Label(cv2, text = priceclick, fg = 'white', bg = '#1f1f1f')
showpricespeed = Label(cv2, text = pricespeed, fg = 'white', bg = '#1f1f1f')

def save(event):
    global balance
    file = open('save_balance_for_miner-game.txt', 'w+')
    file.write(f'{str(balance)}\n{str(click)}\n{str(speed)}\n')
    file.close()

def back():
    global balance, click, speed, priceclick, pricespeed
    file = open('save_balance_for_miner-game.txt', 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i].rstrip()
        lines[i].lstrip()
    balance = int(lines[0])
    click = int(lines[1])
    speed = int(lines[2])
    priceclick = 2**(click//2)
    pricespeed = 2**(speed-1)
    
def clicker():
    global balance, click
    balance += click
    showbal = Label(f1, text = balance, bg = '#1f1f1f', fg = 'white', font = 30)
    showbal.place(x = 150, y = 150, width = 200, height = 50)

def counter():
    global balance, speed
    balance += speed
    showbal = Label(f1, text = balance, bg = '#1f1f1f', fg = 'white', font = 30)
    showbal.place(x = 150, y = 150, width = 200, height = 50)
    sc.after(1000, counter)

def clickkk():
    global click, priceclick, balance
    if priceclick <= balance:
        balance -= priceclick
        click += 2
        priceclick = priceclick*2
        showclick.configure(text = f'{click}\nper click')
        showpriceclick = Label(f2, text = priceclick, fg = 'white', bg = '#1f1f1f')
        showpriceclick.place(x = 150, y = 250, width = 200, height = 50)

def speeddd():
    global speed, pricespeed, balance
    if pricespeed <= balance:
        balance -= pricespeed
        speed += 1
        pricespeed = pricespeed*2
        showspeed.configure(text = f'{speed}\nper second')
        showpricespeed = Label(f2, text = pricespeed, fg = 'white', bg = '#1f1f1f')
        showpricespeed.place(x = 150, y = 450, width = 200, height = 50)

def shopscreen():
    f1.pack_forget()
    clickup = Button(f2, text = '+2 per click',bg = 'yellow', font = 20, command = clickkk)
    speedup = Button(f2, text = '+1 per second',bg = 'yellow', font = 20, command = speeddd)
    back = Button(f2, text = 'back', bg = 'blue', font = 20, command = screen)
    showpriceclick = Label(f2, text = priceclick, fg = 'white', bg = '#1f1f1f')
    showpricespeed = Label(f2, text = pricespeed, fg = 'white', bg = '#1f1f1f')
    f2.pack()
    clickup.place(x = 150, y = 200, width = 200, height = 50)
    speedup.place(x = 150, y = 400, width = 200, height = 50)
    back.place(x = 150, y = 700, width = 200, height = 50)
    showpriceclick.place(x = 150, y = 250, width = 200, height = 50)
    showpricespeed.place(x = 150, y = 450, width = 200, height = 50)

def screen():
    f2.pack_forget()
    showbal = Label(f1, text = balance, bg = '#1f1f1f', fg = 'white', font = 30)
    mine = Button(f1, text = 'CLICK', font = 10, bg = 'yellow', command = clicker)
    shop = Button(f1, text = 'upgrades', bg = 'blue', font = 20, command = shopscreen)
    showspeed = Label(f1, text = f'{speed}\nper second', fg = 'white', bg = '#1f1f1f')
    showclick = Label(f1, text = f'{click}\nper click', fg = 'white', bg = '#1f1f1f')
    f1.pack()
    showbal.place(x = 150, y = 150, width = 200, height = 50)
    mine.place(x = 150, y = 450, width = 200, height = 200)
    showspeed.place(x = 100, y = 200)
    showclick.place(x = 350, y = 200)
    shop.place(x = 150, y = 700, width = 200, height = 50)

    

back()
screen()
counter()
sc.bind('<Destroy>', save)
sc.mainloop()
