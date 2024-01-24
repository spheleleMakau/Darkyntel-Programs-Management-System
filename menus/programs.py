from tkinter import *
from tkinter import ttk


class programClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Darkyntel Management System")
        self.root.geometry("1000x400+80+170")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Manage program Details", font=("goudy old style", 20, "bold"), bg="#fae439", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # programm name widget

        programm_name_label = Label(self.root, text="Program Name:", font=("goudy old style", 10, "bold"), bg="white")
        programm_name_label.place(x=10, y=60)

        self.programm_name_entry = Entry(self.root, font=("goudy old style", 10))
        self.programm_name_entry.place(x=150, y=60, width=300)

        #duration lable and  Entry
        duration_label = Label(self.root, text="Duration:", font=("goudy old style", 10, "bold"), bg="white")
        duration_label.place(x=10, y=100)

        self.duration_entry = Entry(self.root, font=("goudy old style", 10))
        self.duration_entry.place(x=150, y=100, width=300)
        
        # charges lable and  Entry
        charges_label = Label(self.root, text="Charges", font=("goudy old style", 10, "bold"), bg="white")
        charges_label.place(x=10, y=140)

        self.charges_entry = Entry(self.root, font=("goudy old style", 10))
        self.charges_entry.place(x=150, y=140, width=300)

        # description lable and  Entry
        description_label = Label(self.root, text="Description:", font=("goudy old style", 10, "bold"), bg="white")
        description_label.place(x=10, y=180)

        self.description_entry = Entry(self.root, font=("goudy old style", 10))
        self.description_entry.place(x=150, y=180, width=300)




        #Buttons
        Button(self.root, text="Save", font=("goudy old style", 10),bg="#fae439").place(x=150, y=300, width=80)
        Button(self.root, text="Edit", font=("goudy old style", 10),bg="#fae439").place(x=230, y=300, width=80)
        Button(self.root, text="Delete",font=("goudy old style", 10),bg="#fae439").place(x=310, y=300, width=80)
 

        #search
        
        search_program__name_label = Label(self.root, text="Search program:", font=("goudy old style", 10, "bold"), bg="white")
        search_program__name_label.place(x=500, y=60)

        self.var_search=StringVar()
        self.program__name_entry = Entry(self.root,textvariable=self.var_search, font=("goudy old style", 10))
        self.program__name_entry.place(x=650, y=60, width=180)


        self.search_Name_Button=Button(self.root, text="Search", font=("goudy old style", 10),bg="#fae439").place(x=850, y=60, width=120, height=28)
            
   #content
        
        self.program__frame= Frame(self.root,bd=2,relief=RIDGE)
        self.program__frame.place(x=500,y=100,width=470,height=230)

        scrollx = Scrollbar(self.program__frame,orient=HORIZONTAL)
        scrollY = Scrollbar(self.program__frame,orient=VERTICAL)


        self.program_Table= ttk.Treeview(self.program__frame,columns=("pid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrollY.set)
        self.program_Table.pack(fill=BOTH,expand=1)

        #table scrollers
        scrollx.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.program_Table.xview)
        scrollY.config(command=self.program_Table.yview)

        #program_ Table headings
        self.program_Table.heading("pid",text="Program ID")
        self.program_Table.heading("name",text="Name")
        self.program_Table.heading("duration",text="Duration")
        self.program_Table.heading("charges",text="Charges")
        self.program_Table.heading("description",text="Description")
        self.program_Table["show"]="headings"

        #program_ table columns
        self.program_Table.column("pid",width=100)
        self.program_Table.column("name",width=100)
        self.program_Table.column("duration",width=100)
        self.program_Table.column("charges",width=100)
        self.program_Table.column("description",width=150)




if __name__ == "__main__":
    root = Tk()
    obj = programClass(root)
    root.mainloop()
