from tkinter import *
from tkinter import ttk


class ParticipantClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Darkyntel Management System")
        self.root.geometry("1000x400+80+170")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Manage participant Details", font=("goudy old style", 20, "bold"), bg="#2fb8eb", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # participant name widget

        participant_name_label = Label(self.root, text="Participant Name:", font=("goudy old style", 10, "bold"), bg="white")
        participant_name_label.place(x=10, y=60)

        self.participant_name_entry = Entry(self.root, font=("goudy old style", 10))
        self.participant_name_entry.place(x=150, y=60, width=300)

        #Age lable and  Entry
        Age_label = Label(self.root, text="Age:", font=("goudy old style", 10, "bold"), bg="white")
        Age_label.place(x=10, y=100)

        self.Age_entry = Entry(self.root, font=("goudy old style", 10))
        self.Age_entry.place(x=150, y=100, width=300)
        

        #Gender combobox label and entry
        genders = ["Female", "Male"]
        gender_label = Label(self.root, text="Gender:", font=("goudy old style", 10, "bold"), bg="white")
        gender_label.place(x=10, y=140)

        self.gender_combobox = ttk.Combobox(self.root, values=genders, font=("goudy old style", 15))
        self.gender_combobox.place(x=150, y=140, width=300)

        #School combobox label and entry
        schools = ["school A"]
        school_label = Label(self.root, text="School:", font=("goudy old style", 10, "bold"), bg="white")
        school_label.place(x=10, y=180)

        self.school_entry = ttk.Combobox(self.root,values=schools, font=("goudy old style", 10))
        self.school_entry.place(x=150, y=180, width=300)

        #Program combobox label and entry
        program_label = Label(self.root, text="Program:", font=("goudy old style", 10, "bold"), bg="white")
        program_label.place(x=10, y=220)

        self.program_entry = ttk.Combobox(self.root,values=schools, font=("goudy old style", 10))
        self.program_entry.place(x=150, y=220, width=300)

        #Notes lable and  Entry
        notes_label = Label(self.root, text="notes:", font=("goudy old style", 10, "bold"), bg="white")
        notes_label.place(x=10, y=260)

        self.notes_entry = Entry(self.root, font=("goudy old style", 10))
        self.notes_entry.place(x=150, y=260, width=300)




        #Buttons
        Button(self.root, text="Save", font=("goudy old style", 10),bg="#2fb8eb").place(x=150, y=300, width=80)
        Button(self.root, text="Edit", font=("goudy old style", 10),bg="#2fb8eb").place(x=230, y=300, width=80)
        Button(self.root, text="Delete",font=("goudy old style", 10),bg="#2fb8eb").place(x=310, y=300, width=80)
 

        #search
        
        search_gender__name_label = Label(self.root, text="Search Participant:", font=("goudy old style", 10, "bold"), bg="white")
        search_gender__name_label.place(x=500, y=60)

        self.var_search=StringVar()
        self.gender__name_entry = Entry(self.root,textvariable=self.var_search, font=("goudy old style", 10))
        self.gender__name_entry.place(x=650, y=60, width=180)


        self.search_Name_Button=Button(self.root, text="Search", font=("goudy old style", 10),bg="#2fb8eb").place(x=850, y=60, width=120, height=28)
            
   #content
        
        self.gender__frame= Frame(self.root,bd=2,relief=RIDGE)
        self.gender__frame.place(x=500,y=100,width=470,height=230)

        scrollx = Scrollbar(self.gender__frame,orient=HORIZONTAL)
        scrollY = Scrollbar(self.gender__frame,orient=VERTICAL)


        self.gender_Table= ttk.Treeview(self.gender__frame,columns=("ptid","name","Age","gender","school","program"),xscrollcommand=scrollx.set,yscrollcommand=scrollY.set)
        self.gender_Table.pack(fill=BOTH,expand=1)

        #table scrollers
        scrollx.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.gender_Table.xview)
        scrollY.config(command=self.gender_Table.yview)

        #gender_ Table headings
        self.gender_Table.heading("ptid",text="Gender ID")
        self.gender_Table.heading("name",text="Name")
        self.gender_Table.heading("Age",text="Age")
        self.gender_Table.heading("gender",text="Gender")
        self.gender_Table.heading("school",text="School")
        self.gender_Table.heading("program",text="Program")
        self.gender_Table["show"]="headings"

        #gender_ table columns
        self.gender_Table.column("ptid",width=100)
        self.gender_Table.column("name",width=100)
        self.gender_Table.column("Age",width=100)
        self.gender_Table.column("gender",width=100)
        self.gender_Table.column("school",width=100)
        self.gender_Table.column("program",width=100)





if __name__ == "__main__":
    root = Tk()
    obj = ParticipantClass(root)
    root.mainloop()
