from tkinter import *
from PIL import Image, ImageTk
from schools import SchoolClass
import os
# print("Current working directory:", os.getcwd())


class RMS:

    def __init__(self,root) :
        self.root=root
        self.root.title("Darkyntel Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable("false","false")
        self.root.config(bg="white")
    #icons
        self.logo_dash=ImageTk.PhotoImage(file="images/whiteBG-fotor-20240117122732.png")

    # Title
        title=Label(self.root,text="Darkyntel Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#65c0b9",fg="white").place(x=0,y=0,relwidth=1,height=50)

    #Menus
        menuFrame=LabelFrame(self.root,text="menus",font=("times new roman",15),bg="white")
        menuFrame.place(x=10,y=70,width=1340,height=80)

        schools_btn=Button(menuFrame,text="Schools",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2",command=self.add_school).place(x=20,y=5,width=200,height=40)
        program_btn=Button(menuFrame,text="Programs",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2").place(x=240,y=5,width=200,height=40)
        participants_btn=Button(menuFrame,text="Participants",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2").place(x=460,y=5,width=200,height=40)
        partners_btn=Button(menuFrame,text="Partners",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2").place(x=680,y=5,width=200,height=40)
        results_btn=Button(menuFrame,text="Results",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        exit_btn=Button(menuFrame,text="Exit",font=("goudy old style",15,"bold"),bg="#65c0b9",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)

    #content window
        img1 = Image.open("images/Arduino.png").resize((230, 350))
        img2 = Image.open("images/Screenshot from 2024-01-18 01-28-02.png").resize((230, 350))
        img3 = Image.open("images/Drones.png").resize((230, 300))
        img4 = Image.open("images/Lego.png").resize((230, 350))

        # Combine the four images into one row
        combined_img = Image.new("RGB", (920, 350))
        combined_img.paste(img1, (0, 0))
        combined_img.paste(img2, (230, 0))
        combined_img.paste(img3, (460, 0))
        combined_img.paste(img4, (690, 0))

        self.content_img = ImageTk.PhotoImage(combined_img)

        # Content window
        content_label = Label(self.root, image=self.content_img, bg="white")
        content_label.place(x=400, y=180, width=920, height=350)

    #update details
        self.label_school=Label(self.root,text="Total Schools\n[ 0 ]",font=("goudy old style",20),bg="#da62a1",bd=10,relief=RIDGE)
        self.label_school.place(x=400,y=530,width=300,height=100)

        self.label_program=Label(self.root,text="Total Programs\n[ 0 ]",font=("goudy old style",20),bg="#fae439",bd=10,relief=RIDGE)
        self.label_program.place(x=710,y=530,width=300,height=100)
        self.label_participants=Label(self.root,text="Total Participants\n[ 0 ]",font=("goudy old style",20),bg="#2fb8eb",bd=10,relief=RIDGE)
        self.label_participants.place(x=1020,y=530,width=300,height=100)



    def add_school(self):
        self.new_school=Toplevel(self.root)
        self.new_obj=SchoolClass(self.new_school)

    #footer
        footer=Label(self.root,text="DMS- Darkyntel Managment System\nContact Us for any technical Issue: @darkyntel@gmail.com",font=("goudy old style",12),bg="#7a60a6",fg="white").pack(side=BOTTOM,fill=X)

if __name__ =="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()