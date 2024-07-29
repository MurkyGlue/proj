from tkinter import *

st = ''

sc = Tk()
sc['bg'] = '#1f1f1f'
sc.geometry('600x800')
sc.resizable(height = False, width = False)
sc.title('calculator')

def add1():
    global st
    st += '1'
    show.configure(text = st)
def add2():
    global st
    st += '2'
    show.configure(text = st)
def add3():
    global st
    st += '3'
    show.configure(text = st)
def add4():
    global st
    st += '4'
    show.configure(text = st)
def add5():
    global st
    st += '5'
    show.configure(text = st)
def add6():
    global st
    st += '6'
    show.configure(text = st)
def add7():
    global st
    st += '7'
    show.configure(text = st)
def add8():
    global st
    st += '8'
    show.configure(text = st)
def add9():
    global st
    st += '9'
    show.configure(text = st)
def add0():
    global st
    st += '0'
    show.configure(text = st)
def addplus():
    global st
    st += '+'
    show.configure(text = st)
def addminus():
    global st
    st += '-'
    show.configure(text = st)
def addx():
    global st
    st += '*'
    show.configure(text = st)
def adddel():
    global st
    st += '/'
    show.configure(text = st)
def addpoint():
    global st
    st += '.'
    show.configure(text = st)
def result():
    global st, res
    try:
        res = eval(st)
    except SyntaxError:
        st2 = ''
        for i in range(len(st)-1):
            st2 += st[i]
        res = eval(st2)
    st = str(res)
    show.configure(text = res)
def clean():
    global st
    st = ''
    show.configure(text = st)

cv = Canvas(sc, width = 600, height = 800, bg = '#1f1f1f')
show = Label(cv, text = st, bg = '#1f1f1f', font = 50, fg = 'white')
b1 = Button(cv, text = '1', bg = '#3f3f3f', command = add1, fg = 'white', font = 50)
b2 = Button(cv, text = '2', bg = '#3f3f3f', command = add2, fg = 'white', font = 50)
b3 = Button(cv, text = '3', bg = '#3f3f3f', command = add3, fg = 'white', font = 50)
b4 = Button(cv, text = '4', bg = '#3f3f3f', command = add4, fg = 'white', font = 50)
b5 = Button(cv, text = '5', bg = '#3f3f3f', command = add5, fg = 'white', font = 50)
b6 = Button(cv, text = '6', bg = '#3f3f3f', command = add6, fg = 'white', font = 50)
b7 = Button(cv, text = '7', bg = '#3f3f3f', command = add7, fg = 'white', font = 50)
b8 = Button(cv, text = '8', bg = '#3f3f3f', command = add8, fg = 'white', font = 50)
b9 = Button(cv, text = '9', bg = '#3f3f3f', command = add9, fg = 'white', font = 50)
b0 = Button(cv, text = '0', bg = '#3f3f3f', command = add0, fg = 'white', font = 50)
point = Button(cv, text = ',', bg = '#3f3f3f', command = addpoint, fg = 'white', font = 50)
equal = Button(cv, text = '=', bg = '#3f3f3f', command = result, fg = 'white', font = 50)
bplus = Button(cv, text = '+', bg = '#3f3f3f', command = addplus, fg = 'white', font = 50)
bminus = Button(cv, text = '-', bg = '#3f3f3f', command = addminus, fg = 'white', font = 50)
bx = Button(cv, text = '*', bg = '#3f3f3f', command = addx, fg = 'white', font = 50)
bdel = Button(cv, text = '/', bg = '#3f3f3f', command = adddel, fg = 'white', font = 50)
clear = Button(cv, text = 'clear', bg = '#880000', command = clean, fg = 'white', font = 50)

cv.pack()
show.place(x = 0, y = 0, width = 600, height = 250)
b1.place(x = 0, y = 400, width = 200, height = 100)
b2.place(x = 200, y = 400, width = 200, height = 100)
b3.place(x = 400, y = 400, width = 200, height = 100)
b4.place(x = 0, y = 500, width = 200, height = 100)
b5.place(x = 200, y = 500, width = 200, height = 100)
b6.place(x = 400, y = 500, width = 200, height = 100)
b7.place(x = 0, y = 600, width = 200, height = 100)
b8.place(x = 200, y = 600, width = 200, height = 100)
b9.place(x = 400, y = 600, width = 200, height = 100)
b0.place(x = 200, y = 700, width = 200, height = 100)
point.place(x = 0, y = 700, width = 200, height = 100)
equal.place(x = 400, y = 700, width = 200, height = 100)
bplus.place(x = 0, y = 300, width = 150, height = 100)
bminus.place(x = 150, y = 300, width = 150, height = 100)
bx.place(x = 300, y = 300, width = 150, height = 100)
bdel.place(x = 450, y = 300, width = 150, height = 100)
clear.place(x = 0, y = 250, width = 600, height = 50)

sc.mainloop()