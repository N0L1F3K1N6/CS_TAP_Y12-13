from tkinter import*
import tkinter.messagebox
import sqlite3

root = Tk()
root.title("Tournament Application Program")
# Database
con = sqlite3.connect("TAS.db")
cur = con.cursor()
con.commit()
if sqlite3.connect("TAS.db") == False:
    cur.execute("""CREATE TABLE teams (
        Team_name text,
        Team_KD integer,
        Pl_one text,
        Pl_two text,
        Pl_three text,
        Pl_four text,
        Pl_five text
        )""")
else:
    con.close
# Frame Transition
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def show_frame(frame):
    frame.tkraise()

LoginFrame = Frame(root, bg="black")
HubFrame = Frame(root, bg="black")
TeamCreationFrame = Frame(root, bg="black")
TeamApplicationFrame = Frame(root, bg="black")
TeamComparisonFrame = Frame(root, bg="black")
CalenderFrame = Frame(root, bg="black")

for frame in(LoginFrame, HubFrame, TeamCreationFrame, TeamApplicationFrame, TeamComparisonFrame, CalenderFrame):
    frame.grid(row=0, column=0, sticky ="nsew")

# Login Page BackEnd
def Login_command():
    Uname = UNEntry.get()
    Pword = PEntry.get()
    if Uname == "Admin1" and Pword == "Admin1":
        command=show_frame(HubFrame)
        UNEntry.delete(0, END)
        PEntry.delete(0, END)
# Login Page FrontEnd 
Login_title = Label(LoginFrame, text="Please Login", fg="lime", bg="black")
Login_title.grid(row=0)

LoginButton = Button(LoginFrame, text="Login", fg="lime", bg="black", command=Login_command)
LoginButton.grid(row=4)

GLoginButton = Button(LoginFrame, text="Guest Login", fg="lime", bg="black")
GLoginButton.grid(row=4, column=1)

Uname = Label(LoginFrame, text="Username", fg="lime", bg="black")
Pword = Label(LoginFrame, text="Password", fg="lime", bg="black")
Uname.grid(row=1)
Pword.grid(row=2)

UNEntry = Entry(LoginFrame, fg="lime", bg="black")
PEntry = Entry(LoginFrame, fg="lime", bg="black")
UNEntry.grid(row=1, column=1)
PEntry.grid(row=2, column=1)

# Hub BackEnd
def Frame_shift1():
    command=show_frame(TeamCreationFrame)
def Frame_shift2():
    command=show_frame(TeamComparisonFrame)
def Frame_shift3():
    command=show_frame(TeamApplicationFrame)
def Frame_shift4():
    command=show_frame(CalenderFrame)
def Frame_shift5():
    command=show_frame(LoginFrame)
    
# Hub FrontEnd
Hub_title = Label(HubFrame, text="Select a choice", fg="lime", bg="black")
Hub_title.grid(row=0)

TCRButton = Button(HubFrame, text="Team Creation", fg="lime", bg="black", command=Frame_shift1)
TCRButton.grid(row=1, rowspan=2, column=2 , columnspan=3)

TCOButton = Button(HubFrame, text="Team Comparison", fg="lime", bg="black", command=Frame_shift2)
TCOButton.grid(row=1, rowspan=2, column=5, columnspan=6)

TAButton = Button(HubFrame, text="Team Application", fg="lime", bg="black", command=Frame_shift3)
TAButton.grid(row=3, column=2, columnspan=3)

CButton = Button(HubFrame, text="Calender", fg="lime", bg="black", command=Frame_shift4)
CButton.grid(row=3,column=5, columnspan=6)

UCMScroll = Scrollbar(HubFrame)
UCMScroll.grid(row=1, rowspan=4, column=1)

UCMList = Listbox(HubFrame, fg="lime", bg="black", yscrollcommand = UCMScroll.set)
UCMList.grid(row=1, rowspan=4, column=0)

LogButton = Button(HubFrame, text="Logout", fg="lime", bg="black", command=Frame_shift5)
LogButton.grid(row=4, column=5)

# Team Creation BackEnd
def Frame_shiftCR () :
    command=show_frame(HubFrame)

def Sub_data ():
    con = sqlite3.connect("TAS.db")
    cur = con.cursor()
    con.commit()
    cur.execute(" INSERT INTO teams VALUES(:T_Name, :T_KD, :T_Pl1, :T_Pl2, :T_Pl3, :T_Pl4, :T_Pl5)",
                {
                    'T_Name': T_Name.get(),
                    'T_KD': T_KD.get(),
                    'T_Pl1': T_Pl1.get(),
                    'T_Pl2': T_Pl2.get(),
                    'T_Pl3': T_Pl3.get(),
                    'T_Pl4': T_Pl4.get(),
                    'T_Pl5': T_Pl5.get()
                })
    con.close()

# Team Creation FrontEnd
TCr_title = Label(TeamCreationFrame, text="Team Creation", fg="lime", bg="black")
TCr_title.grid(row=0, padx=20, pady=20)

SButton = Button(TeamCreationFrame, text="Submit", fg="lime", bg="black", command=Sub_data)
SButton.grid(row=9, column=0)
RButton = Button(TeamCreationFrame, text="Return", fg="lime", bg="black", command=Frame_shiftCR)
RButton.grid(row=9, column=1)

T_Name = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Name.grid(row=1, column=1)
T_Name_L = Label(TeamCreationFrame, text="Team Name", fg="lime", bg="black")
T_Name_L.grid(row=1, column=0)

T_KD = Entry(TeamCreationFrame, fg="lime", bg="black")
T_KD.grid(row=2, column=1)
T_KD_L = Label(TeamCreationFrame, text="Team KD", fg="lime", bg="black")
T_KD_L.grid(row=2, column=0)

T_Pl1 = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Pl1.grid(row=3, column=1)
T_Pl1_L = Label(TeamCreationFrame, text="Player_1", fg="lime", bg="black")
T_Pl1_L.grid(row=3, column=0)

T_Pl2 = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Pl2.grid(row=4, column=1)
T_Pl2_L = Label(TeamCreationFrame, text="Player_2", fg="lime", bg="black")
T_Pl2_L.grid(row=4, column=0)

T_Pl3 = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Pl3.grid(row=5, column=1)
T_Pl3_L = Label(TeamCreationFrame, text="Player_3", fg="lime", bg="black")
T_Pl3_L.grid(row=5, column=0)

T_Pl4 = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Pl4.grid(row=6, column=1)
T_Pl4_L = Label(TeamCreationFrame, text="Player_4", fg="lime", bg="black")
T_Pl4_L.grid(row=6, column=0)

T_Pl5 = Entry(TeamCreationFrame, fg="lime", bg="black")
T_Pl5.grid(row=7, column=1)
T_Pl5_L = Label(TeamCreationFrame, text="Player_5", fg="lime", bg="black")
T_Pl5_L.grid(row=7, column=0)
# Team Application BackEnd
def Frame_shiftAP () :
    command=show_frame(HubFrame)
# Team Application FrontEnd
TA_title = Label(TeamApplicationFrame, text="Team Application", fg="lime", bg="black")
TA_title.grid(row=0)

RButton = Button(TeamApplicationFrame, text="Return", fg="lime", bg="black", command=Frame_shiftAP)
RButton.grid(row=5, column=1)
AButton = Button(TeamApplicationFrame, text="Apply", fg="lime", bg="black")
AButton.grid(row=5, column=0)

TName = Label(TeamApplicationFrame, text="Team Name", fg="lime", bg="black")
EName = Label(TeamApplicationFrame, text="Event Name", fg="lime", bg="black")
AName = Label(TeamApplicationFrame, text="Approving Admin Name", fg="lime", bg="black")
TName.grid(row=1)
EName.grid(row=2)
AName.grid(row=3)

TNEntry = Entry(TeamApplicationFrame, fg="lime", bg="black")
ENEntry = Entry(TeamApplicationFrame, fg="lime", bg="black")
AAEntry = Entry(TeamApplicationFrame, fg="lime", bg="black")
TNEntry.grid(row=1, column=1)
ENEntry.grid(row=2, column=1)
AAEntry.grid(row=3, column=1)

# Team Comparison BackEnd
def Frame_shiftCO () :
    command=show_frame(HubFrame)
# Team Comparison FrontEnd
TCo_title = Label(TeamComparisonFrame, text="Team Comparison", fg="lime", bg="black")
TCo_title.grid(row=0)

RButton = Button(TeamComparisonFrame, text="Return", fg="lime", bg="black", command=Frame_shiftCO)
RButton.grid(row=5, column=1)

# Calender BackEnd
def Frame_shiftC () :
    command=show_frame(HubFrame)

# Calender FrontEnd
CA_title = Label(CalenderFrame, text="Calendar", fg="lime", bg="black")
CA_title.grid(row=0)

RButton = Button(CalenderFrame, text="Return", fg="lime", bg="black", command=Frame_shiftC)
RButton.grid(row=5, column=1)


show_frame(LoginFrame)
root.mainloop()



# by N0L1F3K1N6
