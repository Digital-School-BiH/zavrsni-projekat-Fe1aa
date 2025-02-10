from tkinter import *
from tkinter import messagebox
from math import floor
from time import strftime
from PIL import Image,ImageTk
from MusicPlayer import musicPlayer
from Calculator import calculatorApp
from ClickerGame import clickerGameApp

def date():
    time=strftime("%A\n%d %b")
    label_date.config(text=time)
    
def clock():
    time=strftime('%H\n%M')
    label_time.config(text=time)
    root.after(1000,clock)
    
def main():
    global label_time
    global label_date
    global root
    
    root=Tk()
    root.title('Phone')
    root.geometry("400x700")
    root.config(bg='#7091e6')
    root.resizable(width=False,height=False)

    frame_title=Frame(root)
    frame_title.config(bg='#adbbda')
    frame_title.pack(padx=10,pady=10)

    label_time=Label(frame_title,font=('times',45,'bold'),justify=CENTER,bg='#adbbda')
    label_time.pack(padx=10)
    clock()

    label_date=Label(frame_title,font=('times',15),justify=CENTER,bg='#adbbda')
    label_date.pack(padx=10)
    date()
    
    frame_apps=Frame(root)
    frame_apps.config(bg='#7091e6')
    frame_apps.pack(padx=10,pady=10)

    icon_c = PhotoImage(file=r"C:\Users\Home\Desktop\Digital School Projekat\Assets\calculator_icon.png")

    calculator=Button(frame_apps,image=icon_c,compound=TOP,command=calculatorApp,bg="#3d52a0")
    calculator.pack(padx=10,pady=10)

    text_c=Label(frame_apps,text="Calculator",font=("Times",15),bg='#adbbda')
    text_c.pack(padx=5,pady=5)

    icon_cg = PhotoImage(file=r"C:\Users\Home\Desktop\Digital School Projekat\Assets\Candy_icon.png")

    clicker_game=calculator=Button(frame_apps,image=icon_cg,compound=TOP,command=clickerGameApp,bg="#3d52a0")
    clicker_game.pack(padx=10,pady=10)

    text_cg=Label(frame_apps,text="Clicker Game",font=("Times",15),bg='#adbbda')
    text_cg.pack(padx=5,pady=5)

    icon_mp=PhotoImage(file=r"C:\Users\Home\Desktop\Digital School Projekat\Assets\MP_icon.png")
    
    music_player=calculator=Button(frame_apps,image=icon_mp,compound=TOP,command=musicPlayer,bg="#3d52a0")
    music_player.pack(padx=10,pady=10)

    text_mp=Label(frame_apps,text="Musicify",font=("Times",15),bg='#adbbda')
    text_mp.pack(padx=5,pady=5)
    
    root.mainloop()

if __name__=="__main__":
    main()
