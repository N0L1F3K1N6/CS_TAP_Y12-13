from tkinter import*
from tkinter import messagebox
import sqlite3


root = Tk()
root.title("Tournament Application Program")

#------------------------------database-------------------------------------------

#con is a variable that creates/connects to the TAS.db File
con = sqlite3.connect("TAP.db")
cur = con.cursor()
cur.execute("""SELECT count(name) FROM sqlite_master WHERE type="table" AND name="Login" """)
#The if statement is used as a verification for the contents of the .db file
if cur.fetchone()[0]==1:
    print("table already exists")
else:
    cur.execute("CREATE TABLE Login(Username TEXT, Password TEXT)")
    cur.execute("""INSERT INTO Login (Username, Password) VALUES ("Admin1", "Admin1")""")
    con.commit()
    cur.execute("CREATE TABLE Teams(Team_Name text, Team_KD integer, P1 text, P2 text, P3 text, P4 text, P5 text)")
    cur.execute("CREATE TABLE Events(Date integer, T1 text, T2 text)")
# Frame Transition
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def show_frame(frame):
    frame.tkraise()

#setting all the frame backgrounds as black before hand
LoginFrame = Frame(root, bg="black")
HubFrame = Frame(root, bg="black")
TeamCreationFrame = Frame(root, bg="black")
TeamApplicationFrame = Frame(root, bg="black")
TeamComparisonFrame = Frame(root, bg="black")
CalenderFrame = Frame(root, bg="black")

#setting all frames to the grid before hand as to make less clutter later on
for frame in(LoginFrame, HubFrame, TeamCreationFrame, TeamApplicationFrame, TeamComparisonFrame, CalenderFrame):
    frame.grid(sticky ="nsew")
   
# Login Page BackEnd
def Login_command():
    Uname = UNEntry.get()
    Pword = PEntry.get()
    RUname = cur.execute(f"""SELECT Username FROM Login WHERE Username == "{Uname}" """)
    RPword = cur.execute(f"""SELECT Password FROM Login WHERE Password == "{Pword}" """)
    con.commit()
    #print(RUname.fetchone()[0])
    print(Pword)
    #print(RPword.fetchall())
    print(RPword)
    if str(Pword) == str(RPword.fetchall()[0][0]) :
        UNEntry.delete(0, END)
        PEntry.delete(0, END)
        command=show_frame(HubFrame)
        print("test")
    else:
        messagebox.showwarning("Error", "Username/Password doesn't match")

def Entry_Register_command():
    Uname = UNEntry.get()
    Pword = PEntry.get()
    print(Uname)
    check = cur.execute(f"""SELECT Username FROM Login WHERE Username == "{Uname}" """)
    # ERROR check.fetchone not an actual command replace this 
    #print(check.fetchone()[0])
    if Uname == check.fetchone()[0]:
        messagebox.showwarning("Error", "Username in use please select a different one")
    else:
        cur.execute(f"""INSERT INTO Login (Username) VALUES "{Uname}" """)
        con.commit()
        cur.execute(f"""INSERT INTO Login (Password) VALUES "{Pword}" """)
        con.commit()
        messagebox.showinfo("Created", "User has been created")
        
    
        
# Login Page FrontEnd 
Login_title = Label(LoginFrame, text="Please Login", fg="lime", bg="black")
Login_title.grid(row=0)

LoginButton = Button(LoginFrame, text="Login", fg="lime", bg="black", command=Login_command)
LoginButton.grid(row=4)

RegButton = Button(LoginFrame, text="Register", fg="lime", bg="black", command=Entry_Register_command)
RegButton.grid(row=4, column=1)

Uname = Label(LoginFrame, text="Username", fg="lime", bg="black")
Pword = Label(LoginFrame, text="Password", fg="lime", bg="black")
Uname.grid(row=1)
Pword.grid(row=2)

UNEntry = Entry(LoginFrame, fg="lime", bg="black")
PEntry = Entry(LoginFrame, fg="lime", bg="black")
UNEntry.grid(row=1, column=1)
PEntry.grid(row=2, column=1)
