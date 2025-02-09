from tkinter import *
from tkinter import messagebox,filedialog
from pygame import mixer
from os import path

def musicPlayer():
    mixer.init()
    global cur_song
    cur_song=""
    global arr
    arr=[]

    def stopSong():
        mixer.music.pause()

    def playSong():
        global cur_song
        song=list_of_songs.get(ANCHOR)
        music_folder=r"C:\Users\Home\Music"
        ind = list_of_songs.curselection()[0]
        try:
            if song:
                if cur_song==song+".mp3" or cur_song==song+".wav":
                    mixer.music.unpause()
                else:
                    to_play=path.join(music_folder,arr[ind])
                    mixer.music.unload()
                    ind=list_of_songs.curselection()[0]
                    song=arr[ind]
                    mixer.music.load(to_play)
                    mixer.music.play()
                    cur_song=song
            else:
                messagebox.showwarning("Warning","No song was selected")
        except Exception as e:
            messagebox.showwarning("Warning",e)
        
    def removeSong():
        song=list_of_songs.get(ANCHOR)
        if song:
            list_of_songs.delete(ANCHOR)
        else:
            messagebox.showwarning("Warning","No song was selected")

    def addSong():
        global arr
        path=filedialog.askopenfilename(title="Select a song",
                                        initialdir=r"C:\Users\Home\Music",
                                        filetypes=[("Audio Files", "*.mp3 *.wav")])
        points=path.split('/')
        core=points[-1].split('.')
        if len(core)>1 and core[1] in ["mp3","wav"]:
            song=core[0]
        else:
            messagebox.showwarning("Warning","Non music file selected or unsupported")
            return
        arr.append(points[-1])
        list_of_songs.insert(END,song)

    def selectNext():
        global cur_song
        global arr
        cur_select = list_of_songs.curselection()
        if cur_select:
            next_ind=cur_select[0]+1
            if next_ind>=list_of_songs.size():
                next_ind=0
                
            list_of_songs.select_clear(0,END)
            list_of_songs.select_set(next_ind)
            list_of_songs.activate(next_ind)
            list_of_songs.see(next_ind)
            list_of_songs.selection_anchor(next_ind)
            
            playSong()
        else:
            messagebox.showwarning("Warning","No song was selected")
            return
            
    def selectPrev():
        global cur_song
        global arr
        cur_select = list_of_songs.curselection()
        if cur_select:
            prev_ind=cur_select[0]-1
            if prev_ind<0:
                prev_ind=list_of_songs.size()-1
                
            list_of_songs.select_clear(0,END)
            list_of_songs.select_set(prev_ind)
            list_of_songs.activate(prev_ind)
            list_of_songs.see(prev_ind)
            list_of_songs.selection_anchor(prev_ind)
            
            playSong()
        else:
            messagebox.showwarning("Warning","No song was selected")
            return

    root = Toplevel()
    root.title("Music Player")
    root.config(bg="#232431")
    root.geometry("400x700")


    frame1 = Frame(root, bg="#232431")
    frame1.grid(row=0,column=0,padx=55)

    list_of_songs = Listbox(frame1,width=20,height=11, selectmode="single",font=("Times", 20),highlightthickness=0,activestyle='none')
    list_of_songs.grid(row=0,column=0)


    frame2 = Frame(root, bg="#232431")
    frame2.grid(row=1,column=0,pady=20)

    button_prev = Button(frame2, text="Prev", font=("Times", 20),command=selectPrev)
    button_prev.grid(row=0, column=0,padx=25,pady=25)

    button_next = Button(frame2, text="Next", font=("Times", 20),command=selectNext)
    button_next.grid(row=0, column=1,padx=25,pady=25)

    button_start = Button(frame2, text="Start", font=("Times", 20),command=playSong)
    button_start.grid(row=1, column=0,padx=25,pady=25)

    button_stop = Button(frame2, text="Stop", font=("Times", 20),command=stopSong)
    button_stop.grid(row=1, column=1,padx=25,pady=25)

    add_button=Button(frame2,text="Add",font=("Times",20),command=addSong)
    add_button.grid(row=2,column=0,padx=25,pady=25)

    remove_button=Button(frame2,text="Remove",font=("Times",20),command=removeSong)
    remove_button.grid(row=2,column=1,padx=25,pady=25)

def main():
    musicPlayer()
    
if __name__=="__main__":
    main()


