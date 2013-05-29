from Tkinter import Tk, Canvas, mainloop

tk = Tk()
w = Canvas(tk, width=600, height=600)

colors = {
    0: 'white', 
    1: 'white', 
    2: 'light yellow', 
    3: 'light yellow', 
    4: 'lemon chiffon', 
    5: 'lemon chiffon', 
    6: 'yellow', 
    7: 'yellow',
    8: 'gold',
    9: 'gold',
    10: 'orange',
    11: 'orange', 
    12: 'orange red',
    13: 'orange red',
    14: 'red',
    15: 'red',
    16: 'red',
    17: 'dark red',
    18: 'dark red',
    19: 'dark red',
    20: 'dark red',
    99: 'black'
}

def mandel(c):
    z = 0
    i = 0
    for h in range(0,20):
        z = z*z + c
        if abs(z) > 2:
            break
        else:
            i+=1
    if abs(z) >= 2:
        return i
    else:
        return 99

print('Drawing...')

for x in range(0,600):
    real = x / 200.0 - 2.2
    for y in range(0, 600):
        imag = y / 200.0 - 1.5
        c = complex(real, imag)
        p = mandel(c)
        w.create_line(x, 600-y, x+1, 601-y, fill=colors[p])
        w.pack()

print ('Complete!')
mainloop()
