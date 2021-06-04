from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registation Window")
        self.root.geometry("1350x700+300+150")
        self.root.config(bg="white")
        #========Bg Imagess===============

        self.bg=ImageTk.PhotoImage(file="Images/BG.jpg")
        bpg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #========Left Imagess===============

        self.left=ImageTk.PhotoImage(file="Images/Signin.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)


        #=============Register Frame==============
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #----------------Row1

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.text_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.text_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_lname.place(x=370,y=130,width=250)

        contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.text_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.text_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_email.place(x=370,y=200,width=250)


        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.text_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_answer.place(x=370,y=270,width=250)



        #===============password================
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.text_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.text_cpassword =Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_cpassword.place(x=370,y=340,width=250)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        
        self.btn_img=ImageTk.PhotoImage(file="Images/start-now-button.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times nwe roman",15),bd=0,cursor="hand2").place(x=235,y=560)


    
    def login_window(self):
        self.root.destroy()
        import login



    def clear(self):
        self.text_fname.delete(0,END)
        self.text_lname.delete(0,END)
        self.text_contact.delete(0,END)
        self.text_email.delete(0,END)
        self.text_answer.delete(0,END)
        self.text_password.delete(0,END)
        self.text_cpassword.delete(0,END)
        self.cmb_quest.current(0)


    def register_data(self):
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.cmb_quest.get()=="Select" or self.text_answer.get()=="" or self.text_password.get()=="" or self.text_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.text_password.get()!=self.text_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)
        else:
            
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="teacher")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.text_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.text_fname.get(),
                                self.text_lname.get(),
                                self.text_contact.get(),
                                self.text_email.get(),
                                self.cmb_quest.get(),
                                self.text_answer.get(),
                                self.text_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()              
            except Exception as es:    
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            







        #print(self.text_fname.get(),
        # self.text_lname.get(),
        # self.text_contact.get(),
        # self.text_email.get(),
        # self.cmb_quest.get(),
        # self.text_answer.get(),
        # self.text_password.get(),
        # self.text_cpassword.get())


        




root = Tk() 
obj = Register(root) 
root.mainloop() 