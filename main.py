from tkinter import *
import pandas as pd

def submit_fields():
    path = 'Game1.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Game Date']
    SeriesB = df1['Opponent']
    SeriesC = df1['Inning']
    SeriesD = df1['Player Name']
    SeriesE = df1['Pitch Type']
    SeriesF = df1['Location']
    SeriesG = df1['Velocity']
    SeriesH = df1['Result']
    SeriesI = df1['Opponent #']


    A = pd.Series(game_date.get())
    B = pd.Series(opponent.get())
    C = pd.Series(inning.get())
    D = pd.Series(p_name.get())
    E = pd.Series(p_type.get())
    F = pd.Series(location.get())
    G = pd.Series(velocity.get())
    H = pd.Series(result.get())
    I = pd.Series(opponent_batter.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)
    SeriesD = SeriesD.append(D)
    SeriesE = SeriesE.append(E)
    SeriesF = SeriesF.append(F)
    SeriesG = SeriesG.append(G)
    SeriesH = SeriesH.append(H)
    SeriesI = SeriesI.append(I)

    df2 = pd.DataFrame({"Game Date": SeriesA, "Opponent": SeriesB, "Inning": SeriesC, "Player Name": SeriesD, "Pitch Type": SeriesE, "Location": SeriesF, "Velocity": SeriesG,
    "Result": SeriesH, "Opponent #": SeriesI})
    df2.to_excel(path, index=False)
    # game_date.delete(0, END)
    # opponent.delete(0, END)
    # inning.delete(0, END)
    # p_name.delete(0, END)
    p_type.delete(0, END)
    location.delete(0, END)
    velocity.delete(0, END)
    result.delete(0, END)
    # opponent_batter.delete(0, END)
    

master = Tk(className="Pitching Data Collection")

Label(master, text="Game Date").grid(row=0)
Label(master, text="Opponent").grid(row=1)
Label(master, text="Inning").grid(row=2)
Label(master, text="Player Name").grid(row=3)
Label(master, text="Pitch Type").grid(row=4)
Label(master, text="Location").grid(row=5)
Label(master, text="Velocity").grid(row=6)
Label(master, text="Result").grid(row=7)
Label(master, text="Opponent #").grid(row=8)

game_date = Entry(master)
opponent = Entry(master)
inning = Entry(master)
p_name = Entry(master)
p_type = Entry(master)
location = Entry(master)
velocity = Entry(master)
result = Entry(master)
opponent_batter = Entry(master)



game_date.grid(row=0, column=1)
opponent.grid(row=1, column=1)
inning.grid(row=2, column=1)
p_name.grid(row=3, column=1)
p_type.grid(row=4, column=1)
location.grid(row=5, column=1)
velocity.grid(row=6, column=1)
result.grid(row=7, column=1)
opponent_batter.grid(row=8, column=1)


Button(master, text='Quit', command=master.quit).grid(row=9, column=0, pady=10)
Button(master, text='Submit', command=submit_fields).grid(row=9, column=1, pady=10)

mainloop()


