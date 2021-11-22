
import requests
import random
from collections import deque
from tkinter import *

#Global Variables
colorToDisplay = ""
color_list = []
color_queue = deque()
w = Tk()
color_entry = StringVar()
hex_argb_color_code = StringVar()


def random_color():
    for j in range(10):
        rand_colors = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(8)])]
        color_list.append(rand_colors)
    colors_list = checkandremoveduplicates(color_list)
    filtered_list = checkforhexspeak(colors_list)
    pushtoQueue(filtered_list)
    

def checkandremoveduplicates(color_list):
    cleaned_list = []
    for i in color_list:
        if i not in cleaned_list or  len(cleaned_list[i]) == len(set(cleaned_list[i])) or cleaned_list[i].find('01234567'):
            cleaned_list.append(i)
    return cleaned_list


def checkforhexspeak(color_list):
    req = requests.get('https://gist.githubusercontent.com/gabrielfalcao/c942f6602401f0697c206e30f0aa4bad/raw/768da56222c1ad3439b3a54879a220aaa699855f/hexspeak')
    hexspeak_list = req.text.split("\n")
    for i in range(len(hexspeak_list)):
        if hexspeak_list[i] in color_list:
            color_list.remove(hexspeak_list[i])
    return color_list
def pushtoQueue(filtered_list):
    [color_queue.append(i) for i in filtered_list]


def popFromQueue():
    try:

        return color_queue.pop()
    except IndexError:
        startMeAgain = random_color()

def apply_color ():
    r = popFromQueue()
    r = "'".join(r)
    hex_argb_color_code.set(r.replace('#','0x'))
    r = r[:-2]
    color_entry.set(r)
    color = color_entry.get()
    w['bg'] = color

def main():
    startMe = random_color()
    
    w.title('Color')
    w.geometry('300x200')

    label = Label(w,textvariable=hex_argb_color_code,anchor=CENTER)
    label.pack()
    button = Button(w,text='Random',width=15,command=apply_color)
    button.pack()
    
    w.mainloop()
# In Case No need to display widget with Color and show output over Terminal. Please enable below line of codes
#    while True:
#        try:
#            text = input("Press Enter for Random:")
#            if text == "":
#                colorToDisplay = popFromQueue()
#                print("'".join(colorToDisplay))
#                print(str(colorToDisplay))
#                w.mainloop()
#
#        except KeyboardInterrupt:
#            print ("Bye")
#            sys.exit()

if __name__ == "__main__":
    main()