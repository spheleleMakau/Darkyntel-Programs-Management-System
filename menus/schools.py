from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry



class SchoolClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Darkyntel Management System")
        self.root.geometry("1000x400+80+170")
        self.root.resizable(False, False)
        self.root.config(bg="white")

    
        # Title
        title = Label(self.root, text="Manage School Details", font=("goudy old style", 20, "bold"), bg="#65c0b9", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # school name widget

        school_name_label = Label(self.root, text="School Name:", font=("goudy old style", 10, "bold"), bg="white")
        school_name_label.place(x=10, y=60)

        self.school_name_entry = Entry(self.root, font=("goudy old style", 10))
        self.school_name_entry.place(x=150, y=60, width=300)

        # Location lable and  Entry
        location_label = Label(self.root, text="Location:", font=("goudy old style", 10, "bold"), bg="white")
        location_label.place(x=10, y=100)

        self.location_entry = Entry(self.root, font=("goudy old style", 10))
        self.location_entry.place(x=150, y=100, width=300)

        #programs combobox label and entry
        programs = ["Program A", "Program B", "Program C"]  # Replace with your program options
        program_label = Label(self.root, text="Program:", font=("goudy old style", 10, "bold"), bg="white")
        program_label.place(x=10, y=140)

        self.program_combobox = ttk.Combobox(self.root, values=programs, font=("goudy old style", 15))
        self.program_combobox.place(x=150, y=140, width=300)

        # Date Entry
        date_label = Label(self.root, text="Date:", font=("goudy old style", 10, "bold"), bg="white")
        date_label.place(x=10, y=180)

        self.date_entry = DateEntry(self.root, font=("goudy old style", 10), background="darkblue", foreground="white", borderwidth=2)
        self.date_entry.place(x=150, y=180, width=300)

        # Description Entry
        description_label = Label(self.root, text="Description:", font=("goudy old style", 10, "bold"), bg="white")
        description_label.place(x=10, y=220)

        self.description_entry = Entry(self.root, font=("goudy old style", 10))
        self.description_entry.place(x=150, y=220, width=300,height=40)

        # Participants Entry
        participants_label = Label(self.root, text="Participants:", font=("goudy old style", 10, "bold"), bg="white")
        participants_label.place(x=10, y=260)

        self.participants_entry = Entry(self.root, font=("goudy old style", 10))
        self.participants_entry.place(x=150, y=260, width=300)

        #Buttons
        Button(self.root, text="Save", font=("goudy old style", 10),bg="#65c0b9").place(x=150, y=300, width=80)
        Button(self.root, text="Edit", font=("goudy old style", 10),bg="#65c0b9").place(x=230, y=300, width=80)
        Button(self.root, text="Delete",font=("goudy old style", 10),bg="#65c0b9").place(x=310, y=300, width=80)
 
    #search
        
        search_school_name_label = Label(self.root, text="Search School:", font=("goudy old style", 10, "bold"), bg="white")
        search_school_name_label.place(x=500, y=60)

        self.var_search=StringVar()
        self.school_name_entry = Entry(self.root,textvariable=self.var_search, font=("goudy old style", 10))
        self.school_name_entry.place(x=620, y=60, width=180)


        self.search_Name_Button=Button(self.root, text="Search", font=("goudy old style", 10),bg="#65c0b9").place(x=850, y=60, width=120, height=28)
            
   #content
        
        self.school_frame= Frame(self.root,bd=2,relief=RIDGE)
        self.school_frame.place(x=500,y=100,width=470,height=230)

        scrollx = Scrollbar(self.school_frame,orient=HORIZONTAL)
        scrollY = Scrollbar(self.school_frame,orient=VERTICAL)


        self.schoolTable= ttk.Treeview(self.school_frame,columns=("sid","name","location","program","participants","description"),xscrollcommand=scrollx.set,yscrollcommand=scrollY.set)
        self.schoolTable.pack(fill=BOTH,expand=1)

        #table scrollers
        scrollx.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.schoolTable.xview)
        scrollY.config(command=self.schoolTable.yview)

        #School Table headings
        self.schoolTable.heading("sid",text="School ID")
        self.schoolTable.heading("name",text="Name")
        self.schoolTable.heading("location",text="Location")
        self.schoolTable.heading("program",text="Program")
        self.schoolTable.heading("participants",text="Participants")
        self.schoolTable.heading("description",text="Description")
        self.schoolTable["show"]="headings"

        #School table columns
        self.schoolTable.column("sid",width=100)
        self.schoolTable.column("name",width=100)
        self.schoolTable.column("location",width=100)
        self.schoolTable.column("program",width=100)
        self.schoolTable.column("participants",width=100)
        self.schoolTable.column("description",width=150)


if __name__ == "__main__":
    root = Tk()
    obj = SchoolClass(root)
    root.mainloop()