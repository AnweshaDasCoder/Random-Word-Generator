from tkinter import *
import random

root = Tk()
root.title("Random Word Generator")
root.geometry("400x400")
root.configure(background="pink")

word_label = Label(root, text="")
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def word():
    random1 = random.randint(0, 52)
    random2 = random.randint(0, 52)
    random3 = random.randint(0, 52)
    random4 = random.randint(0, 52)
    random5 = random.randint(0, 52)
    
    random_no1 = list1[random1]
    random_no2 = list1[random2]
    random_no3 = list1[random3]
    random_no4 = list1[random4]
    random_no5 = list1[random5]
    
    word_label["text"] += str(random_no1) + str(random_no2) + str(random_no3) + str(random_no4) + str(random_no5)
    
def reset():
    word_label["text"] = ""

btn1 = Button(root, text="What Will Your Word Be? ", command = word)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

btn2 = Button(root, text="Reset", command = reset)
btn2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
