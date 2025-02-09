from tkinter import *
from math import floor
from tkinter import messagebox

def clickerGameApp():
    global score_total, change, cost_click, cost_glove, glove_count
    def Load_game():
        niz = []
        with open("Save.txt") as file:
            for line in file:
                separate = line.split(":")
                num = separate[1].strip('\n')
                niz.append(num)
        return niz

    niz = Load_game()
    score_total = float(niz[0])
    change = int(niz[1])
    cost_click = int(niz[2])
    cost_glove = int(niz[3])
    glove_count = int(niz[4])

    def Click():
        global score_total
        score_total += change
        score.config(text=str(score_total))

    def Update():
        global score_total, glove_count
        score_total += glove_count / 2
        if score_total == floor(score_total):
            score_total = floor(score_total)
        score.config(text=str(score_total))
        root_cg.after(500, Update)

    def Upgrade(num):
        global cost_click, cost_glove, change, score_total, glove_count

        if num == 0:  
            if cost_click <= score_total:
                score_total -= cost_click
                change *= 2
                cost_click = round(cost_click * 1.05 ** change)
                score.config(text=str(score_total))
                cost_text.config(text=f"Cost {str(cost_click)}\n{change}x")
            else:
                messagebox.showwarning('Warning', 'Insufficient funds')

        elif num == 1:  
            if cost_glove <= score_total:
                score_total -= cost_glove
                glove_count += 1
                cost_glove += glove_count * 2  
                score.config(text=str(score_total))
                glove_cost_text.config(text=str(cost_glove))
            else:
                messagebox.showwarning('Warning', 'Insufficient funds')

    def Save_game():
        global cost_click, cost_glove, change, score_total, glove_count
        saves = [score_total, change, cost_click, cost_glove, glove_count]
        names = ["score_total", "change", "cost_click", "cost_glove", "glove_count"]
        with open('Save.txt', 'w') as file:
            for i in range(len(saves)):
                string = f'{names[i]}:{saves[i]}\n'
                file.write(string)
        messagebox.showinfo('Saved', 'Your game has been saved')

    root_cg = Toplevel()
    root_cg.title('Candy Clicker')
    root_cg.config(bg='white')
    root_cg.geometry("400x500")

    frame = Frame(root_cg)
    frame.grid(row=0, column=0, pady=10, padx=150)
    frame.config(bg='white')

    score = Label(frame, font=('times', 24, 'bold'), bg='white', text=str(score_total))
    score.grid(row=0, column=0)

    root_cg.icon = PhotoImage(file=r"C:\Users\Home\Desktop\Digital School Projekat\Assets\Candy.png")
    button = Button(frame, image=root_cg.icon, compound=TOP, command=Click)
    button.grid(row=1, column=0, sticky=W)

    frame_up = Frame(root_cg)
    frame_up.grid(row=1, column=0, pady=10, padx=150)
    frame_up.config(bg='white')

    upgrade_btn = Button(frame_up, text="Upgrade", font=('times', 15), command=lambda: Upgrade(0))
    upgrade_btn.grid(row=3, column=0)

    cost_text = Label(frame_up, text=f"Cost {str(cost_click)}\n{change}x", font=('times', 15), bg='white')
    cost_text.grid(row=2, column=0, pady=5)

    frame_glove = Frame(root_cg)
    frame_glove.grid(row=2, column=0, pady=10, padx=150)
    frame_glove.config(bg='white')

    glove_btn = Button(frame_glove, text="Buy Glove", font=('times', 15), command=lambda: Upgrade(1))
    glove_btn.grid(row=5, column=0)

    glove_cost_text = Label(frame_glove, text=str(cost_glove), font=('times', 15), bg='white')
    glove_cost_text.grid(row=4, column=0, pady=5)

    save_btn = Button(root_cg, text="Save", font=('times', 15), command=Save_game)
    save_btn.grid(row=6, column=0, pady=40)
    Update()

def main():
    clickerGameApp()

if __name__=="__main__":
    main()
