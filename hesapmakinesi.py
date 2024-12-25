import tkinter as tk

def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.delete(0, tk.END)
        sonuc.insert(0,str(s1+s2))
def cikar():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.delete(0, tk.END)
        sonuc.insert(0,str(s1-s2))
def carpma():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.delete(0, tk.END)
        sonuc.insert(0,str(s1*s2))
def bolme():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.delete(0, tk.END)
        sonuc.insert(0,str(s1/s2))

pencere = tk.Tk()
pencere.title('E.Z Hesap Makinesi')
pencere.minsize(450,600)

sonuc = tk.Entry(pencere,font=5,width=8)
sonuc.place(x=250, y=70)
sayi1 = tk.Entry(pencere,font=5,width=8)
sayi1.place(x=50,y=70)
sayi2 = tk.Entry(pencere,font=5,width=8)
sayi2.place(x=150,y=70)

button1 = tk.Button(pencere, text="+", width=2, command=topla)
button1.place(x=100, y=150)
button2 = tk.Button(pencere, text="-", width=2, command=cikar)
button2.place(x=150, y=150)
button3 = tk.Button(pencere, text="*",  width=2, command=carpma)
button3.place(x=200, y=150)
button4 = tk.Button(pencere, text="/",  width=2, command=bolme)
button4.place(x=250, y=150)

sayi1.focus()

pencere.mainloop()
