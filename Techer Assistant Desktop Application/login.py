from tkinter import*
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Techer Assistant")
        self.root.geometry("1350x700+300+150")


        
        

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        

        #===========Frame============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("time nwe Roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("time nwe Roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("time nwe Roman",15,),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("time nwe Roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("time nwe Roman",15,),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)



        self.left_=ImageTk.PhotoImage(file="Images/Signin.jpg")
        left_=Label(self.root,image=self.left_).place(x=80,y=100,width=400,height=500)


        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times nwe roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("times nwe roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)
        
    
    def register_window(self):
        self.root.destroy()
        import register


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
             try:
                 con=pymysql.connect(host="localhost",user="root",password="",database="teacher")
                 cur=con.cursor()
                 cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)                     
                 else:
                     messagebox.showinfo("Success","Welcome",parent=self.root)
                     self.root.destroy()
                     import student
                 con.close()    
             except Exception as es:
                 messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)       




root=Tk()
obj=Register(root)
root.mainloop()    