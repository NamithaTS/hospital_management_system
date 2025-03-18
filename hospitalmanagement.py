from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root 
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")


        self.NameofTablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issueddate=StringVar()
        self.Expirydate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()  
        self.Drivingusingmachine=StringVar()
        self.medication=StringVar()
        self.PatientID=StringVar()
        self.nhsnumber=StringVar()
        self.PatientName=StringVar()
        self.dateofbirth=StringVar()
        self.PatientAdress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management system",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #dataframe

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="Patient information" )

        DataframeLeft.place(x=0,y=5,width=950,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="prescription" )

        DataframeRight.place(x=930,y=5,width=400,height=350) 

        #buttons
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1400,height=70)

        #detailsframe
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1400,height=190)

        lblNameTablet=Label(DataframeLeft,text="Names of tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.NameofTablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNameTablet["values"]=("nice","Corona Vaccine","acetaminophen","amlodipine","ativan")
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        
        lblnot=Label(DataframeLeft,font=("arial",12,"bold"),text="No of tablets:",padx=2,pady=4)
        lblnot.grid(row=3,column=0,sticky=W)
        txtnot=Entry(DataframeLeft, textvariable=self.NumberofTablets, font=("arial",12,"bold"),width=35)
        txtnot.grid(row=3,column=1)

        
        lbllot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=4)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        txtlot.grid(row=4,column=1)

        
        lblissuedate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=4)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissdate=Entry(DataframeLeft,textvariable=self.Issueddate,font=("arial",12,"bold"),width=35)
        txtissdate.grid(row=5,column=1)

        lblexpirydate=Label(DataframeLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=4)
        lblexpirydate.grid(row=6,column=0,sticky=W)
        txtexpdate=Entry(DataframeLeft,textvariable=self.Expirydate,font=("arial",12,"bold"),width=35)
        txtexpdate.grid(row=6,column=1)

        lbldd=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lbldd.grid(row=7,column=0,sticky=W)
        txtdd=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        txtdd.grid(row=7,column=1)

        lblsideff=Label(DataframeLeft,font=("arial",12,"bold"),text="side effect:",padx=2,pady=4)
        lblsideff.grid(row=8,column=0,sticky=W)
        txtsideff=Entry(DataframeLeft,textvariable=self.sideEffect,font=("arial",12,"bold"),width=35)
        txtsideff.grid(row=8,column=1)

        lblfurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further information:",padx=2,pady=4)
        lblfurtherinfo.grid(row=0,column=2,sticky=W)
        txtfurtherinfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtfurtherinfo.grid(row=0,column=3)

        lblbp=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood pressure:",padx=2,pady=4)
        lblbp.grid(row=1,column=2,sticky=W)
        txtbp=Entry(DataframeLeft,textvariable=self.Drivingusingmachine,font=("arial",12,"bold"),width=35)
        txtbp.grid(row=1,column=3)

        lblslab=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage advice:",padx=2,pady=4)
        lblslab.grid(row=2,column=2,sticky=W)
        txtslab=Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtslab.grid(row=2,column=3)

        lblmed=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=4)
        lblmed.grid(row=3,column=2,sticky=W)
        txtmed=Entry(DataframeLeft,textvariable=self.medication,font=("arial",12,"bold"),width=35)
        txtmed.grid(row=3,column=3)

        lblpid=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=4)
        lblpid.grid(row=4,column=2,sticky=W)
        txtpid=Entry(DataframeLeft,textvariable=self.PatientID,font=("arial",12,"bold"),width=35)
        txtpid.grid(row=4,column=3)

        lblnhs=Label(DataframeLeft,font=("arial",12,"bold"),text="NHs No:",padx=2,pady=4)
        lblnhs.grid(row=5,column=2,sticky=W)
        txtnhs=Entry(DataframeLeft,textvariable=self.nhsnumber,font=("arial",12,"bold"),width=35)
        txtnhs.grid(row=5,column=3)

        lblpname=Label(DataframeLeft,font=("arial",12,"bold"),text="patient name",padx=2,pady=4)
        lblpname.grid(row=6,column=2,sticky=W)
        txtpname=Entry(DataframeLeft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        txtpname.grid(row=6,column=3)

        lbldob=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=4)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob=Entry(DataframeLeft,textvariable=self.dateofbirth,font=("arial",12,"bold"),width=35)
        txtdob.grid(row=7,column=3)

        lblpadd=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=4)
        lblpadd.grid(row=8,column=2,sticky=W)
        txtpadd=Entry(DataframeLeft,textvariable=self.PatientAdress,font=("arial",12,"bold"),width=35)
        txtpadd.grid(row=8,column=3)


        #right df

        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=40 ,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)


        #buttons
        btnpres = Button(Buttonframe,command=self.ipre, text="prescription", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btnpres.grid(row=0,column=0)

        btnpresdata = Button(Buttonframe,command=self.ipres, text="prescription data", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btnpresdata.grid(row=0,column=1)

        btnupdate = Button(Buttonframe,command=self.update_data, text="update", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btnupdate.grid(row=0,column=2)


        btndel = Button(Buttonframe, command=self.idele,text="Delete", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btndel.grid(row=0,column=3)


        btnclr = Button(Buttonframe, command=self.clear,text="clear", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btnclr.grid(row=0,column=4)


        btnexit = Button(Buttonframe, command=self.iexit,text="exit", bg="green", fg="white",
                 font=("arial", 12, "bold"),width=21, padx=2, pady=6)

        btnexit.grid(row=0,column=5)


        #scroll bar
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expirydate","dailydose","storage",
                                                               "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expirydate",text="Expiry date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHs number")
        self.hospital_table.heading("pname",text="patient Name")
        self.hospital_table.heading("dob",text="Date of birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
      

        self.hospital_table.column("nameoftablets",width=110)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=110)
        self.hospital_table.column("expirydate",width=110)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=110)


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #functions
    def ipres(self):
        if self.NameofTablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","all fields are necessary")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Nami@2004",database="Mydata")
            my_cursor=conn.cursor()

            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.NameofTablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issueddate.get(),
                self.Expirydate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                
                self.nhsnumber.get(),
                self.PatientName.get(),
                self.dateofbirth.get(),
                self.PatientAdress.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nami@2004",database="Mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("update hospital set nameoftablets=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expirydate=%s,dailydose=%s,storage=%s,nhsnumber=%s,pname=%s,dob=%s,address=%s where ref=%s",(
                self.NameofTablets.get(),
               
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issueddate.get(),
                self.Expirydate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsnumber.get(),
                self.PatientName.get(),
                self.dateofbirth.get(),
                self.PatientAdress.get(),
                self.ref.get(),
            ))
        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nami@2004",database="Mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()   
        conn.close()

    def get_cursor(self):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issueddate.set(row[5])
        self.Expirydate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsnumber.set(row[9])
        self.PatientName.set(row[10])
        self.dateofbirth.set(row[11])
        self.PatientAdress.set(row[12])


    def ipre(self):

        self.txtprescription.insert(END,"nameoftablets\t\t\t" +self.NameofTablets.get()+ "\n" ) 
        self.txtprescription.insert(END,"ref\t\t\t" +self.ref.get()+ "\n" )  
        self.txtprescription.insert(END,"dose\t\t\t" +self.Dose.get()+ "\n" ) 
        self.txtprescription.insert(END,"number of tablets\t\t\t" +self.NumberofTablets.get()+ "\n" )  
        self.txtprescription.insert(END,"lot\t\t\t" +self.Lot.get()+ "\n" )
        self.txtprescription.insert(END,"issue date\t\t\t" +self.Issueddate.get()+ "\n" )
        self.txtprescription.insert(END,"exp date\t\t\t" +self.Expirydate.get()+ "\n" ) 
        self.txtprescription.insert(END,"daily dose\t\t\t" +self.DailyDose.get()+ "\n" ) 
        self.txtprescription.insert(END,"side effect\t\t\t" +self.sideEffect.get()+ "\n" ) 
        self.txtprescription.insert(END,"further information\t\t\t" +self.FurtherInformation.get()+ "\n" ) 
        self.txtprescription.insert(END,"storage\t\t\t" +self.StorageAdvice.get()+ "\n" ) 
        self.txtprescription.insert(END,"driving\t\t\t" +self.Drivingusingmachine.get()+ "\n" ) 
        self.txtprescription.insert(END,"patient id\t\t\t" +self.PatientID.get()+ "\n" ) 
        self.txtprescription.insert(END,"nhsnumber\t\t\t" +self.nhsnumber.get()+ "\n" ) 
        self.txtprescription.insert(END,"patient name\t\t\t" +self.PatientName.get()+ "\n" ) 
        self.txtprescription.insert(END,"dateof birth\t\t\t" +self.dateofbirth.get()+ "\n" ) 
        self.txtprescription.insert(END,"patient address\t\t\t" +self.PatientAdress.get()+ "\n" ) 


    def idele(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nami@2004",database="Mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data
        messagebox.showinfo("delete","patient deleted")


    def clear(self):
        self.NameofTablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issueddate.set("")
        self.Expirydate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.Drivingusingmachine.set("")
        self.medication.set("")
        self.PatientID.set("")
        self.nhsnumber.set("")
        self.PatientName.set("")
        self.dateofbirth.set("")
        self.PatientAdress.set("")
        self.txtprescription.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("hospital management system","confirm to exit")
        if iexit>0:
            root.destroy()
            return













root=Tk()
ob=Hospital(root)
root.mainloop()