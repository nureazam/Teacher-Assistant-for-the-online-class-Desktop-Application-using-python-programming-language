from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1800x770+50+150")


        title=Label(self.root,text="Teacher Assistant",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="#074463",fg="white")
        title.pack(side=TOP,fill=X)

        title=Label(self.root,text="North South University Teacher Assistant DeskTop AP For Online Class",bd=10,relief=GROOVE,font=("time new roman",18,"bold"),bg="#074463",fg="white")
        title.pack(side=BOTTOM,fill=X)



      #===========All Variables=========================

        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        



  


      #==========Manage Frame==========================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#074463")
        Manage_Frame.place(x=20,y=100,width=450,height=600)



        m_title=Label(Manage_Frame,text="Manage Students",bg="#074463",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Student ID",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(Manage_Frame,text="Full Name",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_email=Label(Manage_Frame,text="Email",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_gender=Label(Manage_Frame,text="Gender",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)


        lbl_contact=Label(Manage_Frame,text="Contact",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_dob=Label(Manage_Frame,text="Assignment",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        lbl_address=Label(Manage_Frame,text="All Exam",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        
        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10,"bold"))
        self.txt_Address.grid(row=7,column=1,padx=20,pady=10,sticky="w")

      #=========Button Frome===========================
        Button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#074463")
        Button_Frame.place(x=15,y=520,width=420)

        Add_Button=Button(Button_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Update_Button=Button(Button_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Delete_Button=Button(Button_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clear_Button=Button(Button_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

      #=========Detail Frome===========================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#074463")
        Detail_Frame.place(x=500,y=100,width=800,height=600)



        lbl_search=Label(Detail_Frame,text="Search By",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")


        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)


        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")


        search_btn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)



      #============Table Frame=========================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#074463")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Student ID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="Assignment")
        self.Student_table.heading("address",text="Quiz & Mid & Final Exam")


        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=350)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()


#=================Assignment Frame=====================================
        Assignment_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#074463")
        Assignment_Frame.place(x=1330,y=100,width=450,height=600)


        m_title=Label(Assignment_Frame,text="Short Note For Teacher",bg="#074463",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #lbl_teacher=Label(Assignment_Frame,text="Student ID",bg="#074463",fg="white",font=("times new roman",20,"bold"))
        #lbl_teacher.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Teacher=Text(Assignment_Frame,width=35,height=18,font=("",15,"bold"))
        txt_Teacher.grid(row=1,column=1,padx=20,pady=10,sticky="w")

        #txt_Teacher=Entry(Assignment_Frame,width=40,height=5,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_Teacher.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        







    def add_students(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
      self.name_var.get(),
      self.email_var.get(),
      self.gender_var.get(),
      self.contact_var.get(),
      self.dob_var.get(),
      self.txt_Address.get('1.0',END)
      ))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()

        


    def fetch_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("select * from students")
      rows=cur.fetchall()
      if len(rows)!=0:
        self.Student_table.delete(*self.Student_table.get_children())
        for row in rows:
          self.Student_table.insert('',END,values=row)
        con.close()   

    def clear(self):
      self.roll_no_var.set("")
      self.name_var.set("")
      self.email_var.set("")
      self.gender_var.set("")
      self.contact_var.set("")
      self.dob_var.set("")
      self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
      cursor_row=self.Student_table.focus()
      contents=self.Student_table.item(cursor_row)
      row=contents['values']

      self.roll_no_var.set(row[0])
      self.name_var.set(row[1])
      self.email_var.set(row[2])
      self.gender_var.set(row[3])
      self.contact_var.set(row[4])
      self.dob_var.set(row[5])
      self.txt_Address.delete("1.0",END)
      self.txt_Address.insert(END,row[6])

    def update_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
      self.name_var.get(),
      self.email_var.get(),
      self.gender_var.get(),
      self.contact_var.get(),
      self.dob_var.get(),
      self.txt_Address.get('1.0',END),
      self.roll_no_var.get()
      ))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()
    

    def delete_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
      con.commit()
      con.close()
      self.fetch_data()
      self.clear()

    
    def search_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()

      cur.execute("select * from students where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
      rows=cur.fetchall()
      if len(rows)!=0:
        self.Student_table.delete(*self.Student_table.get_children())
        for row in rows:
          self.Student_table.insert('',END,values=row)
        con.close()  



root=Tk()
ob=Student(root)
root.mainloop()
