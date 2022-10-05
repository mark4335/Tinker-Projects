# Name: Mark Waako


from tkinter import *
root = Tk()
root.title("Title")
root.configure(bg="white")
label1 = Label(root, text ="My first name is Mark.", bg="light blue" ,fg="black", font="arial 40" )
label1.pack()
label2 = Label(root, text ="My last name is Waako.", bg="light blue" ,fg="black", font="arial 40" )
label2.pack()
label3 = Label(root, text ="My faculty i Science.", bg="light blue" ,fg="black", font="arial 40" )
label3.pack()
label4 = Label(root, text ="my year is 1.", bg="light blue" ,fg="black", font="arial 40" )
label4.pack()


root.mainloop()


