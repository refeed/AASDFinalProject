from tkinter import *
import csv

with open('Book1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


window = Tk()
window.title("FINAL PROJECT AASD KELOMPOK 3")


window.minsize(width=1920, height=1080)
window.config(padx=100,pady=50, bg="#f7f5dd")

title_label = Label(text="Rekomendas Produk E-commerce", fg="#9bdeac", bg="#f7f5dd", font=("Arial", 50))
title_label.grid(column=1, row=0, columnspan=7)

count = 0
for i in range(4):
    if i == 3:
        for j in range(2):
            button = Button(text=data[count][0], highlightthickness=0,wraplength=80)
            button.grid(column=j, row=i+1, sticky = W+E+N+S)
            button.config(padx=80, pady=20)
            count +=1
    else:
        for j in range(7):
            button = Button(text=data[count][0], highlightthickness=0,wraplength=80)
            button.grid(column=j, row=i+1, sticky = W+E+N+S)
            button.config(padx=80, pady=20)
            count+=1


rekomendasi_label = Label(text="Rekomendasi", fg="black", bg="#f7f5dd", font=("Arial", 50))
rekomendasi_label.grid(column=1, row=5, columnspan=7)





window.mainloop()
