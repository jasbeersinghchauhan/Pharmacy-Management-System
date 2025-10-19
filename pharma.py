from tkinter import*     # importing gui library
from tkinter import ttk     #This line imports the ttk (Themed Tkinter) module, which is part of the standard tkinter library in Python.
                            # It allows you to use modern, themed widgets that look more native to the operating system.
import mysql.connector 
from tkinter import messagebox











class PharmacyManagementSystem:
    def __init__(self,root):  #This is the constructor method in Python.  It is automatically called when you create an instance of the class.
                              #self refers to the current instance of the class.  root is the main Tkinter window that will be passed in when creating the object.

       self.root=root
       self.root.title("Pharmacy Management System")
       self.root.geometry("1550x800+0+0")    #This sets the size and position of the main window.  Format:"widthxheight+x_offset+y_offset"   Width = 1550 pixels
                                             #Height = 800 pixels  X offset = 0 (distance from left edge of the screen)    Y offset = 0 (distance from top of the screen)
                                             #In other words, the window will open in the top-left corner of the screen and will be 1550×800 pixels large







       self.addmed_var=StringVar()
       self.refMed_var=StringVar()

   



       self.ref_var=StringVar()
       self.cmpName_var=StringVar()
       self.typeMed_var=StringVar()
       self.medName_var=StringVar()
       self.lot_var=StringVar()
       self.issuedate_var=StringVar()
       self.expdate_var=StringVar()





       
       lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='lightblue',fg="blue",font=("times new roman",50,"bold"),padx=2,pady=4)
                                              #bd=15	The border width of the label (15 pixels thick).
                                              #relief=RIDGE	The border style. RIDGE gives a 3D ridged border effect. Other options include FLAT, SUNKEN, RAISED, GROOVE, etc.
                                              #bg='white'	The background color of the label.
                                              #fg='darkgreen'	The foreground (text) color of the label

       lbltitle.pack(side=TOP,fill=X)             #side=TOP	Positions the label at the top of the window.
                                                  #fill=X	Makes the label stretch horizontally (across the entire width of the window).










      
       DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)  #This line creates a Frame widget — a rectangular container used to group other widgets(like labels,buttons, or entry fields).
                                                              #Think of a Frame as a “section” or “box” within your main window where you can neatly organize related items.

       DataFrame.place(x=0,y=120,width=1530,height=400)       #This line positions the frame within your main window using the place() geometry manager.
                                                              #Tkinter has three geometry managers:
                                                              #pack() – stacks widgets vertically or horizontally
                                                              #grid() – places widgets in a table-like structure
                                                              #place() – positions widgets by absolute coordinates (x, y)












       DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",bg='lightblue',fg="blue",font=("arial",12,"bold")) 
       # A LabelFrame is a special type of Frame that has a title (label) at the top.
       # Parameter=DataFrame ,Purpose=Parent container for this subframe.

       DataFrameLeft.place(x=0,y=5,width=900,height=350)       

       DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",bg='lightblue',fg="blue",font=("arial",12,"bold"))  

       DataFrameRight.place(x=910,y=5,width=540,height=350)















       ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)  

       ButtonFrame.place(x=0,y=520,width=1530,height=65) 


       










       btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add ",bg='lightgreen',fg="green",font=("arial",12,"bold"))  

       btnAddData.grid(row=0,column=0)

       btnUpdateData=Button(ButtonFrame,text="UPDATE ",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14)  

       btnUpdateData.grid(row=0,column=1) 

       btnDeleteData=Button(ButtonFrame,text="DELETE ",bg='red',fg="white",font=("arial",13,"bold"),width=14)  

       btnDeleteData.grid(row=0,column=2) 
 
       btnRestMed=Button(ButtonFrame,text="RESET",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14)  

       btnRestMed.grid(row=0,column=3) 

       btnExitMed=Button(ButtonFrame,text="EXIT ",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14)  

       btnExitMed.grid(row=0,column=4)  














    
       lblSearch=Label(ButtonFrame,text="Search By ",bg='white',padx=2,fg="black",font=("arial",17,"bold"))  

       lblSearch.grid(row=0,column=5,sticky=W)   #sticky=W means “align the widget to the West (left) side of its grid cell.”


      







   

       search_combo = ttk.Combobox(ButtonFrame, width=16, font=("arial", 13, "bold"), state="readonly")
       search_combo["values"] = ("Ref", "Medicine Name", "Lot")
       search_combo.grid(row=0, column=6)
       search_combo.current(0)
       #search_combo.current(0)
       #This sets the default selected value to the first item in the list ("Ref").
       #So when the program starts, “Ref” will automatically appear selected.
 








       txtSearch = Entry(ButtonFrame, bd=3, relief=RIDGE, width=12, font=("arial", 17, "bold"))
       txtSearch.grid(row=0, column=7)
       searchBtn = Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
       searchBtn.grid(row=0, column=8)
       showAll=Button(ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
       showAll.grid(row=0, column=9)














       
       lblrefno = Label(DataFrameLeft, text="Reference No", font=("arial", 12, "bold"), padx=2, fg="black")
       lblrefno.grid(row=0, column=0, sticky=W)

       # Database connection and fetch for the main Reference No Combobox (DataFrameLeft)
       try:
            conn = mysql.connector.connect(host="localhost", username="root", password="mysqlpassword1@", database="trial")
            my_cursor = conn.cursor()
            
            # --- FIX: Execute the query before fetching ---
            my_cursor.execute("SELECT Ref FROM pharma") # Assuming Ref column holds the reference numbers
            
            rows = my_cursor.fetchall()
            
            # Convert the list of tuples (rows) into a flat list for the Combobox
            ref_values = [item[0] for item in rows] if rows else ["Select Ref"]
            
            conn.close()

       except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to load Reference Numbers: {err}")
            ref_values = ["Error Loading"]


       

       ref_combo = ttk.Combobox(DataFrameLeft,textvariable=self.ref_var, width=27, font=("arial", 17, "bold"), state="readonly")
       ref_combo["values"] = ref_values # Use the fetched/error list
       ref_combo.grid(row=0, column=1)
       ref_combo.current(0)

       





       








        
       lblcn = Label(DataFrameLeft,text="Company Name:", font=("arial", 12, "bold"), padx=2, pady=6)
       lblcn.grid(row=1, column=0, sticky=W)
       txtcn = Entry(DataFrameLeft,textvariable=self.cmpName_var, bd=2, relief=RIDGE, width=29, font=("arial", 13, "bold"))
       txtcn.grid(row=1, column=1)












  
       lblTypeofMedicine = Label(DataFrameLeft, text="Type Of Medicine", font=("arial", 12, "bold"), padx=2, pady=6)
       lblTypeofMedicine.grid(row=2, column=0, sticky=W)

       comTypeofMedicine = ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var, width=27, font=("arial", 12, "bold"), state="readonly")
       comTypeofMedicine['value'] = ("Tablet", "Liquid", "Capules", "Syrup", "Inhales", "Injection")
       comTypeofMedicine.grid(row=2, column=1)
       











       lblMedicineName = Label(DataFrameLeft, text="Medicine Name", font=("arial", 12, "bold"), padx=2, pady=6)
       lblMedicineName.grid(row=3, column=0, sticky=W)

       conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="trial")
       my_cursor=conn.cursor()
       my_cursor.execute("select MedName from pharma")
       med=my_cursor.fetchall()
       
       comMedicineName = ttk.Combobox(DataFrameLeft,textvariable=self.medName_var, width=27, font=("arial", 12, "bold"), state="readonly")
       comMedicineName['value'] = med
       comMedicineName.grid(row=3, column=1)
       comMedicineName.current(0)












       lblLotNo = Label(DataFrameLeft, text="Lot No:", font=("arial", 12, "bold"), padx=2, pady=6)
       lblLotNo.grid(row=4, column=0, sticky=W)
       txtLotNo = Entry(DataFrameLeft,textvariable=self.lot_var, bd=2, relief=RIDGE, width=29, font=("arial", 13, "bold"))
       txtLotNo.grid(row=4, column=1)












       lblIssueDate = Label(DataFrameLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
       lblIssueDate .grid(row=5, column=0, sticky=W)
       txtIssueDate = Entry(DataFrameLeft,textvariable=self.issuedate_var, bd=2, relief=RIDGE, bg="white", width=29, font=("arial", 13, "bold"))
       txtIssueDate .grid(row=5, column=1)










       
       lblExpDate = Label(DataFrameLeft, text="Exp Date:", font=("arial", 12, "bold"), padx=2, pady=6)
       lblExpDate .grid(row=6, column=0, sticky=W)
       txtExpDate = Entry(DataFrameLeft, textvariable=self.expdate_var,bd=2, relief=RIDGE, bg="white", width=29, font=("arial", 13, "bold"))
       txtExpDate .grid(row=6, column=1)
 










       lblrefno = Label(DataFrameRight, text="Reference No:", font=('arial', 12, 'bold'))
       lblrefno.place(x=0, y=80)
       txtrefno = Entry(DataFrameRight,textvariable=self.refMed_var, font=('arial', 15, 'bold'), bg="white", bd=2, relief=RIDGE, width=14)
       txtrefno.place(x=135, y=80)

       lblmedName = Label(DataFrameRight, font=('arial', 12, 'bold'), text="Medicine Name:")
       lblmedName.place(x=0, y=110)
       txtmedName = Entry(DataFrameRight,textvariable=self.addmed_var, font=('arial', 15, 'bold'), bg="white", bd=2, relief=RIDGE, width=14)
       txtmedName.place(x=135, y=110)

       
       side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
       side_frame.place(x=0, y=150, width=290, height=160)

       sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
       sc_x.pack(side=BOTTOM, fill=X)
       sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
       sc_y.pack(side=RIGHT, fill=Y)
       # fill=X or fill=Y makes them stretch along their respective sides

       self.medicine_table = ttk.Treeview(side_frame, columns=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

       sc_x.config(command=self.medicine_table.xview)
       sc_y.config(command=self.medicine_table.yview)

       self.medicine_table.heading("ref", text="Reference No")
       self.medicine_table.heading("medname", text="Medicine Name")

       self.medicine_table["show"] = "headings"
       self.medicine_table.pack(fill=BOTH, expand=1)   # pack(fill=BOTH, expand=1) makes it expand to fill the frame.

       self.medicine_table.column("ref", width=100)
       self.medicine_table.column("medname", width=100)


       # ====================== Medicine Add Buttons ======================
       down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
       down_frame.place(x=330, y=150, width=135, height=160)

       btnAddmed = Button(down_frame, text="ADD", font=('arial', 12, 'bold'), width=12, bg="darkgreen", fg="white", pady=4,command=self.AddMed)
       btnAddmed.grid(row=0, column=0)

       btnUpdatemed = Button(down_frame, text="UPDATE", font=('arial', 12, 'bold'), width=12, bg="purple", fg="white", pady=4)
       btnUpdatemed.grid(row=1, column=0)

       btnDeletemed = Button(down_frame, text="DELETE", font=('arial', 12, 'bold'), width=12, bg="red", fg="white", pady=4)
       btnDeletemed.grid(row=2, column=0)

       btnClearmed = Button(down_frame, text="CLEAR", font=('arial', 12, 'bold'), width=12, bg="orange", fg="white", pady=4)
       btnClearmed.grid(row=3, column=0)

       #====================FRAME DETAILS=========================
       FrameDetails = Frame(self.root, bd=15, relief=RIDGE)
       FrameDetails.place(x=0, y=580, width=1530, height=210)

       #===================== Main Table & scrollbar ======================
       Table_frame = Frame(self.root, bd=15, relief=RIDGE,padx=20)
       Table_frame.place(x=0, y=600, width=1500, height=180)

       scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
       scroll_y.pack(side=RIGHT, fill=Y)

       self.pharmacy_table = ttk.Treeview(Table_frame, column=("reg", "companyname", "type", "tabletname", "lotno", "issuedate", "expdate"), xscrollcommand=scroll_x.set,           yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.pharmacy_table.xview)
       scroll_y.config(command=self.pharmacy_table.yview)

       self.pharmacy_table["show"] = "headings"

       self.pharmacy_table.heading("reg", text="Reference No")
       self.pharmacy_table.heading("companyname", text="Company Name")
       self.pharmacy_table.heading("type", text="Type of Medicine")
       self.pharmacy_table.heading("tabletname", text="Tablet Name")
       self.pharmacy_table.heading("lotno", text="Lot No")
       self.pharmacy_table.heading("issuedate", text="Issue Date")
       self.pharmacy_table.heading("expdate", text="Exp Date")
       self.pharmacy_table.pack(fill=BOTH,expand=1)
       self.fetch_dataMed()








    def AddMed(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="trial")
           my_cursor=conn.cursor()
           my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(self.refMed_var.get(),self.addmed_var.get() ))

           conn.commit()
           self.fetch_dataMed()
           conn.close()
           messagebox.showinfo("Success","Medicine has been added successfully")











    def fetch_dataMed(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="trial")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from pharma")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
              self.medicine_table.delete(*self.medicine_table.get_children())
              for i in rows:
                  self.medicine_table.insert("",END,values=i)

              conn.commit()
           conn.close()  
                                                                              








    def add_data(self):
           
           conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="trial")
           my_cursor=conn.cursor()
           my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s)",(self.ref_var.get() ,self.cmpName_var.get(),self.typeMed_var.get(),self.medName_var.get(),self.lot_var .get(),self.issuedate_var.get(),self.expdate_var.get()))

           conn.commit()
           self.fetch_dataMed()
           conn.close()
           messagebox.showinfo("Success","Data has been added successfully")











if __name__=="__main__":         #This checks whether the file is being run directly or imported as a module.   When a Python file is executed directly, __name_ is set to "_main_".
                                 #This ensures that the code inside this block only runs when the script is executed directly — not when imported.

    root=Tk()   #tkinter object created named "root". root is the name of our window
    obj=PharmacyManagementSystem(root)
    root.mainloop()   #makes the window open continously