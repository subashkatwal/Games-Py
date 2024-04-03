from tkinter import *
def storyfirst(win):
    def final(tl: Toplevel,name,Sports,City,playerName,drinkName,snacks):
        text=f'''
        Hi my name is {name}.I live in {City} and my favorite Sports is {Sports}.I like to watch {playerName} with enjoying {drinkName}.
        Its funny but I like {snacks} rather than drinks .
        '''
        tl.geometry(newGeometry='500x550')
        Label(tl,text='Story:',wraplength=tl.winfo_width()).place(x=600,y=310)
        Label(tl,text=text,wraplength=tl.winfo_width()).place(x=0,y=330)
        
    NewScreen=Toplevel(win,bg='blue')
    NewScreen.title("A memorable day !")
    NewScreen.geometry('500x500')
    
    Label(NewScreen,text='Memorable Day ').place(x=100,y=0)
    Label(NewScreen,text='Name').place(x=0,y=35)
    Label(NewScreen,text='City').place(x=0,y=70)
    Label(NewScreen,text='Sports').place(x=0,y=105)
    Label(NewScreen,text='Player Name').place(x=0,y=140)
    Label(NewScreen,text='Drink Name ').place(x=0,y=175)
    Label(NewScreen,text='Snacks ').place(x=0,y=210)
    
    Name=Entry(NewScreen,width=22)
    Name.place(x=250,y=35)
    
    sports=Entry(NewScreen,width=22)
    sports.place(x=250,y=70)
    
    city=Entry(NewScreen,width=22)
    city.place(x=250,y=105)
    
    player_name=Entry(NewScreen,width=22)
    player_name.place(x=250,y=140)
    
    drink=Entry(NewScreen,width=22)
    drink.place(x=250,y=175)
    
    snacks=Entry(NewScreen,width=22)
    snacks.place(x=250,y=210)
    
    SubmitButton=Button(NewScreen,text="Submit",background="Aqua",font=("Times",12),
                        command=lambda:final(NewScreen,Name.get(),sports.get(),city.get(),player_name.get(),
                                             drink.get(),snacks.get()))
    SubmitButton.place(x=150,y=300)
    
    NewScreen.mainloop()
Screen=Tk()
Screen.title("Welcome to my game")
Screen.geometry('400x400')
Screen.config(bg='Lime')
Label(Screen,text="Subash Katwal ").place(x=100,y=20)

#buttons 
firstButton=Button(Screen,text="memorable day ",font=("Times New Roman",15),command=lambda:storyfirst(Screen),bg='Aqua')
firstButton.place(x=150,y=90)

Screen.update()
Screen.mainloop()
                    
    