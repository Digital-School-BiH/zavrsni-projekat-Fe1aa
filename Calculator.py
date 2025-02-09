from tkinter import *
from math import floor
def calculatorApp():
    #calculator application
    def calculate(sign):
        equation=entry.get()
        if sign=='C':
            entry.delete(0,END)
        elif sign=='=':
            try:
                result=eval(equation)
                if floor(result) == result:
                    result=floor(result)
                else:
                    result=round(result,2)
                entry.delete(0,END)
                entry.insert(END,str(result))
            except (ZeroDivisionError,SyntaxError,NameError):
                entry.delete(0,END)
                entry.insert(END,'Error')
        else:
            if sign in '+-*/' and equation[-1] in '+-*/':
                entry.delete(len(equation)-1,END)
                
            entry.insert(END,sign)

    root_c=Toplevel()
    root_c.title('Calculator')
    root_c.resizable(width=False,height=False)
    frame_output=Frame(root_c)
    frame_output.pack(fill=X)

    entry=Entry(frame_output,relief="solid",font=("Times New Roman",30),justify="right")
    entry.grid(column=0,row=0,columnspan=4,padx=10,pady=10)

    frame_input=Frame(root_c)
    frame_input.pack(fill=X)

    keyboard=['7','8','9','/',
              '4','5','6','*',
              '1','2','3','-',
              'C','0','=','+'
    ]

    col=0
    row=0
    for i in keyboard:
        button=Button(frame_input,text=i,font=("Times New Roman",14),width=7,height=3,command=lambda f=i:calculate(f))
        button.grid(row=row,column=col,padx=14,pady=10)
        col+=1
        if col==4:
            col=0
            row+=1
            
def main():
    calculatorApp()

if __name__=="__main__":
    main()
