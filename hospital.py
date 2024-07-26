from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # *************************** DataFrame *****************************
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1350, height=380)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=930, height=340)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=931, y=5, width=370, height=340)

        # ************************** Buttons Frame ******************************
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=510, width=1350, height=70)

        # ************************** Details Frame ******************************
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=580, width=1350, height=150)

        # *************************** DataFrameLeft ***********************************
        lblNameTablet = Label(DataFrameLeft, text="Name Of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Refence No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.ref, width=32)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Dose,width=32)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=32)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=32)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=32)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Expdate, width=32)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose, width=32)
        txtDailyDose.grid(row=7, column=1)

        lblsideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.sideEffect, width=32)
        txtsideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.FurtherInformation, width=32)
        txtFurtherInfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DrivingUsingMachine, width=32)
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.StorageAdvice, width=32)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.HowToUseMedication, width=32)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientId, width=32)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.nhsNumber, width=32)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientName, width=32)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DateOfBirth, width=32)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientAddress, width=32)
        txtPatientAddress.grid(row=8, column=3)

        # **************************** DataFrameRight ***********************************
        self.textPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=34, height=15, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0)

        # ***************************** Buttons *********************************
        button_color = "#228B22"  # Lighter shade of green
        btnPrescription = Button(ButtonFrame, command=self.iPrescription, text="Prescription", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(ButtonFrame, command=self.iPrescriptionData, text="Prescription Data", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(ButtonFrame, command=self.update_data, text="Update", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(ButtonFrame, command=self.idetele, text="Delete", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnclear = Button(ButtonFrame,command=self.clear, text="Clear", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnclear.grid(row=0, column=4)

        btnExit = Button(ButtonFrame,command=self.iExit, text="Exit", bg=button_color, fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ***********************************Table***********************************

        # *************************************Scrollbar***************************
        # ***************************** Table Frame ***********************************
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
 
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.grid(row=1, column=0, sticky="ew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        self.hospital_table.grid(row=0, column=0, sticky="nsew")

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        DetailsFrame.grid_rowconfigure(0, weight=1)
        DetailsFrame.grid_columnconfigure(0, weight=1)

        self.hospital_table.heading("nameoftable", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()




# *******************************************Functionality Declaration *******************************
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
            my_cursor=conn.cursor() 
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(), 
                self.Expdate.get(),
                self.DailyDose.get(), 
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor() 
        my_cursor.execute("update hospital set Nameoftablets=%s, Dose=%s, No_Of_Tablets=%s, Lot=%s, Issue_Date=%s, Exp_Date=%s, Daily_Dose=%s, Storage=%s, NHSNumber=%s, Patinet_Name=%s, DOB=%s, Address=%s where Reference_No=%s",(
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(), 
                self.Expdate.get(),
                self.DailyDose.get(), 
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
            ))

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall() 
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        self.textPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.textPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.textPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
        self.textPrescription.insert(END,"Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.textPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
        self.textPrescription.insert(END,"Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.textPrescription.insert(END,"exp date:\t\t\t" + self.Expdate.get() + "\n")
        self.textPrescription.insert(END,"daily dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.textPrescription.insert(END,"side effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.textPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.textPrescription.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.textPrescription.insert(END,"DrivingUsingMachine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.textPrescription.insert(END,"PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.textPrescription.insert(END,"NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n")
        self.textPrescription.insert(END,"PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.textPrescription.insert(END,"dateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.textPrescription.insert(END,"PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")


    def idetele(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor() 
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("") 
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.textPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy() 
            return


root = Tk()
ob = Hospital(root)
root.mainloop()
