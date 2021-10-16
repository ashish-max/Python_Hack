from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="mothersday.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0,  relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="mothersday.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100,  width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        f_name = Label(frame1, text="First Name", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=100)
        txt_fname = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=390, y=100)
        txt_lname = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=390, y=130, width=250)

        phone = Label(frame1, text="Contact Number", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=170)
        txt_phone = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=50, y=200, width=250)

        email = Label(frame1, text="Email Id", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=390, y=170)
        txt_email = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=390, y=200, width=250)

        question = Label(frame1, text="Security Question", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=240)
        cmb_quest = ttk.Combobox(frame1, font=("times new roman", 15), state="readonly", justify=CENTER)
        cmb_quest["values"]=("Select", "Your Pet Name", "First School Name","Favourite Food", "Other")
        cmb_quest.place(x=50, y=270, width=250)
        cmb_quest.current(0)
        answer = Label(frame1, text="Answer", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=390, y=240)
        txt_answer = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=390, y=270, width=250)

        Password = Label(frame1, text="Password", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=310)
        txt_password = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=390, y=310)
        txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="light gray").place(x=390, y=340, width=250)

        chk = Checkbutton(frame1, text="I Agree To The Terms & Conditions", onvalue=1, offvalue=0, font=("times new roman", 12), bg="white").place(x=50, y=380)

        btn = Button(frame1, text="Register", font=("times new roman", 15), fg="white", bg="green").place(x=300, y=440)


root=Tk()
obj=Register(root)
root.mainloop()
