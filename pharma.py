from tkinter import* # importing gui library
from tkinter import ttk     #This line imports the ttk (Themed Tkinter) module, which is part of the standard tkinter library in Python.
                              # It allows you to use modern, themed widgets that look more native to the operating system.
import mysql.connector 
from tkinter import messagebox



class PharmacyManagementSystem:
    def __init__(self,root):  #This is the constructor method in Python.  It is automatically called when you create an instance of the class.
                              #self refers to the current instance of the class.  root is the main Tkinter window that will be passed in when creating the object.

        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")    #This sets the size and position of the main window.  Format:"widthxheight+x_offset+y_offset"    Width = 1550 pixels
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
        self.quantity_var = StringVar() # New variable to store medicine quantity

        
        
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()
        
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='lightblue',fg="blue",font=("times new roman",50,"bold"),padx=2,pady=4)
                                          #bd=15    The border width of the label (15 pixels thick).
                                          #relief=RIDGE    The border style. RIDGE gives a 3D ridged border effect. Other options include FLAT, SUNKEN, RAISED, GROOVE, etc.
                                          #bg='white'    The background color of the label.
                                          #fg='darkgreen'    The foreground (text) color of the label

        lbltitle.pack(side=TOP,fill=X)        #side=TOP    Positions the label at the top of the window.
                                              #fill=X    Makes the label stretch horizontally (across the entire width of the window).



        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)  #This line creates a Frame widget — a rectangular container used to group other widgets(like labels,buttons, or entry fields).
                                                              #Think of a Frame as a “section” or “box” within your main window where you can neatly organize related items.

        DataFrame.place(x=0,y=120,width=1530,height=400)      #This line positions the frame within your main window using the place() geometry manager.
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

        btnUpdateData=Button(ButtonFrame,text="UPDATE ",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14, command=self.update_data)  

        btnUpdateData.grid(row=0,column=1) 

        btnDeleteData=Button(ButtonFrame,text="DELETE ",bg='red',fg="white",font=("arial",13,"bold"),width=14, command=self.delete_data)  

        btnDeleteData.grid(row=0,column=2) 
 
        btnRestMed=Button(ButtonFrame,text="RESET",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14, command=self.reset_data)  

        btnRestMed.grid(row=0,column=3) 

        btnExitMed=Button(ButtonFrame,text="EXIT ",bg='lightgreen',fg="green",font=("arial",13,"bold"),width=14, command=self.exit_app)  

        btnExitMed.grid(row=0,column=4)  


        
        lblSearch=Label(ButtonFrame,text="Search By ",bg='white',padx=2,fg="black",font=("arial",17,"bold"))  

        lblSearch.grid(row=0,column=5,sticky=W)    #sticky=W means “align the widget to the West (left) side of its grid cell.”


        
        search_combo = ttk.Combobox(ButtonFrame, textvariable=self.search_by_var, width=16, font=("arial", 13, "bold"), state="readonly")
        search_combo["values"] = ("Ref", "Medicine Name", "Lot", "Quantity") # Added Quantity
        search_combo.grid(row=0, column=6)
        search_combo.current(0)
        #This sets the default selected value to the first item in the list ("Ref").
        #So when the program starts, “Ref” will automatically appear selected.
 


        txtSearch = Entry(ButtonFrame, textvariable=self.search_txt_var, bd=3, relief=RIDGE, width=12, font=("arial", 17, "bold"))
        txtSearch.grid(row=0, column=7)
        searchBtn = Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.search_data)
        searchBtn.grid(row=0, column=8)
        showAll=Button(ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white", command=self.fetch_data_main)
        showAll.grid(row=0, column=9)



        
        lblrefno = Label(DataFrameLeft, text="Reference No", font=("arial", 12, "bold"), padx=2, fg="black")
        lblrefno.grid(row=0, column=0, sticky=W)

        
        
        self.ref_combo = ttk.Combobox(DataFrameLeft,textvariable=self.ref_var, width=27, font=("arial", 17, "bold"), state="readonly") # This is the combobox for Ref No
        self.ref_combo.grid(row=0, column=1)

        


        
        
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

        
        
        self.comMedicineName = ttk.Combobox(DataFrameLeft,textvariable=self.medName_var, width=27, font=("arial", 12, "bold"), state="readonly") # This is the combobox for Med Name
        self.comMedicineName.grid(row=3, column=1)

        
        self.update_comboboxes() # This function is called to load data into the comboboxes above
        
        
        
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
 
        
        
               
        
        
        lblQuantity = Label(DataFrameLeft, text="Quantity:", font=("arial", 12, "bold"), padx=2, pady=6) # New label for Quantity
        lblQuantity .grid(row=7, column=0, sticky=W)
        txtQuantity = Entry(DataFrameLeft, textvariable=self.quantity_var, bd=2, relief=RIDGE, bg="white", width=29, font=("arial", 13, "bold")) # New entry for Quantity
        txtQuantity .grid(row=7, column=1)
 
  
 
 
 
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
        self.medicine_table.pack(fill=BOTH, expand=1)    # pack(fill=BOTH, expand=1) makes it expand to fill the frame.

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)
        self.medicine_table.bind("<ButtonRelease-1>", self.get_cursor_med) # Binds a click event to the get_cursor_med function


        # ====================== Medicine Add Buttons ======================
        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        down_frame.place(x=330, y=150, width=135, height=160)

        btnAddmed = Button(down_frame, text="ADD", font=('arial', 12, 'bold'), width=12, bg="darkgreen", fg="white", pady=4,command=self.AddMed)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed = Button(down_frame, text="UPDATE", font=('arial', 12, 'bold'), width=12, bg="purple", fg="white", pady=4, command=self.update_med)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed = Button(down_frame, text="DELETE", font=('arial', 12, 'bold'), width=12, bg="red", fg="white", pady=4, command=self.delete_med)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed = Button(down_frame, text="CLEAR", font=('arial', 12, 'bold'), width=12, bg="orange", fg="white", pady=4, command=self.clear_med)
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

        self.pharmacy_table = ttk.Treeview(Table_frame, column=("reg", "companyname", "type", "tabletname", "lotno", "issuedate", "expdate", "quantity"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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
        self.pharmacy_table.heading("quantity", text="Quantity")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("reg", width=100) # Setting column widths for alignment
        self.pharmacy_table.column("companyname", width=200)
        self.pharmacy_table.column("type", width=150)
        self.pharmacy_table.column("tabletname", width=200)
        self.pharmacy_table.column("lotno", width=120)
        self.pharmacy_table.column("issuedate", width=120)
        self.pharmacy_table.column("expdate", width=120)
        self.pharmacy_table.column("quantity", width=80) # New column width for Quantity
        
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor_main) # Binds a click event to get_cursor_main
        
        self.fetch_dataMed() # Loads data into the side table on startup
        self.fetch_data_main() # Loads data into the main table on startup









    def update_comboboxes(self): # This function reloads the data in the left-side comboboxes
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="mysqlpassword1@", database="pharmacy")
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT Ref FROM pharma") # Get all Ref numbers
            rows_ref = my_cursor.fetchall()
            ref_values = [item[0] for item in rows_ref] if rows_ref else [""]
            
            my_cursor.execute("SELECT MedName FROM pharma") # Get all Medicine Names
            rows_med = my_cursor.fetchall()
            med_values = [item[0] for item in rows_med] if rows_med else [""]
            
            conn.close()
            
            self.ref_combo['values'] = ref_values # Update the Ref combobox list
            self.comMedicineName['values'] = med_values # Update the MedName combobox list
            
            if ref_values:
                self.ref_combo.current(0)
            if med_values:
                self.comMedicineName.current(0)
                
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to load combobox data: {err}")










    def AddMed(self): # Function for the "ADD" button on the right side
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(self.refMed_var.get(),self.addmed_var.get() ))

                conn.commit()
                self.fetch_dataMed() # Refreshes the right-side table
                self.update_comboboxes() # Refreshes the left-side comboboxes
                self.clear_med() # Clears the entry boxes
                conn.close()
                messagebox.showinfo("Success","Medicine has been added successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")







    def fetch_dataMed(self): # Function to load data into the right-side table
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from pharma")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.medicine_table.delete(*self.medicine_table.get_children()) # Clears the table first
                for i in rows:
                    self.medicine_table.insert("",END,values=i) # Inserts each row

                conn.commit()
            conn.close()  
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error fetching medicine data: {err}")
            
            
            
            
            
            
            
            
            
    def get_cursor_med(self, event=""): # Called when a row is clicked in the right-side table
        cursor_row = self.medicine_table.focus() # Gets the clicked row
        content = self.medicine_table.item(cursor_row)
        row = content.get("values", [])
        if row:
            self.refMed_var.set(row[0]) # Populates the entry boxes with data from the row
            self.addmed_var.set(row[1])
            
            
           
            
            
            
            
            
    def update_med(self): # Function for the "UPDATE" button on the right side
        if self.refMed_var.get() == "":
            messagebox.showerror("Error", "Reference No is required to update")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE pharma SET MedName=%s WHERE Ref=%s", (
                    self.addmed_var.get(),
                    self.refMed_var.get()
                ))
                conn.commit()
                self.fetch_dataMed() # Refreshes the right-side table
                self.update_comboboxes() # Refreshes the left-side comboboxes
                self.clear_med() # Clears the entry boxes
                conn.close()
                messagebox.showinfo("Success", "Medicine has been updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
                
                
                
                
                
                
                
                
    def delete_med(self): # Function for the "DELETE" button on the right side
        if self.refMed_var.get() == "":
            messagebox.showerror("Error", "Reference No is required to delete")
        else:
            mDelete = messagebox.askyesno("Delete", "Do you want to delete this medicine?", parent=self.root)
            if mDelete > 0:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                    my_cursor=conn.cursor()
                    my_cursor.execute("DELETE FROM pharma WHERE Ref=%s", (self.refMed_var.get(),))
                    conn.commit()
                    self.fetch_dataMed() # Refreshes the right-side table
                    self.update_comboboxes() # Refreshes the left-side comboboxes
                    self.clear_med() # Clears the entry boxes
                    conn.close()
                    messagebox.showinfo("Delete", "Medicine has been deleted")
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
            else:
                return
                
                                
                
                
                
                
                
    def clear_med(self): # Function for the "CLEAR" button on the right side
        self.refMed_var.set("")
        self.addmed_var.set("")
        
        
        
       
        
        
        
        
    def add_data(self): # Function for the main "Medicine Add" button in the ButtonFrame
        if self.ref_var.get() == "" or self.lot_var.get() == "" or self.medName_var.get() == "" or self.quantity_var.get() == "":
            messagebox.showerror("Error", "Ref, Med Name, Lot No, and Quantity are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s)",( # Added %s for quantity
                    self.ref_var.get() ,
                    self.cmpName_var.get(),
                    self.typeMed_var.get(),
                    self.medName_var.get(),
                    self.lot_var.get(),
                    self.issuedate_var.get(),
                    self.expdate_var.get(),
                    self.quantity_var.get() # Added quantity variable
                ))

                conn.commit()
                self.fetch_data_main() # Refreshes the main bottom table
                self.reset_data() # Clears the left-side form
                conn.close()
                messagebox.showinfo("Success","Data has been added successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}. Check if quantity is a number.")
                
                
                
                
                
                
                
                
                
    def fetch_data_main(self): # Function to load data into the main bottom table
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from pharmacy")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children()) # Clears the table first
                for i in rows:
                    self.pharmacy_table.insert("",END,values=i) # Inserts each row
                conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error fetching pharmacy data: {err}")
            
                       
            
            
            
            
            
            
            
    def get_cursor_main(self, event=""): # Called when a row is clicked in the main bottom table
        cursor_row = self.pharmacy_table.focus() # Gets the clicked row
        content = self.pharmacy_table.item(cursor_row)
        row = content.get("values", [])
        if row:
            self.ref_var.set(row[0]) # Populates the left-side form with data from the row
            self.cmpName_var.set(row[1])
            self.typeMed_var.set(row[2])
            self.medName_var.set(row[3])
            self.lot_var.set(row[4])
            self.issuedate_var.set(row[5])
            self.expdate_var.set(row[6])
            self.quantity_var.set(row[7]) # Added quantity
            
            
            
           
            
            
            
            
            
    def update_data(self): # Function for the main "UPDATE" button in the ButtonFrame
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Reference No is required to update")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE pharmacy SET companyname=%s, type=%s, tabletname=%s, lotno=%s, issuedate=%s, expdate=%s, quantity=%s WHERE reg=%s", ( # Added quantity
                    self.cmpName_var.get(),
                    self.typeMed_var.get(),
                    self.medName_var.get(),
                    self.lot_var.get(),
                    self.issuedate_var.get(),
                    self.expdate_var.get(),
                    self.quantity_var.get(), # Added quantity
                    self.ref_var.get()
                ))
                conn.commit()
                self.fetch_data_main() # Refreshes the main bottom table
                self.reset_data() # Clears the left-side form
                conn.close()
                messagebox.showinfo("Success", "Data has been updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
                
                
                
                
                
                
                
                
                
    def delete_data(self): # Function for the main "DELETE" button in the ButtonFrame
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Reference No is required to delete")
        else:
            mDelete = messagebox.askyesno("Delete", "Do you want to delete this record?", parent=self.root)
            if mDelete > 0:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
                    my_cursor=conn.cursor()
                    my_cursor.execute("DELETE FROM pharmacy WHERE reg=%s", (self.ref_var.get(),))
                    conn.commit()
                    self.fetch_data_main() # Refreshes the main bottom table
                    self.reset_data() # Clears the left-side form
                    conn.close()
                    messagebox.showinfo("Delete", "Record has been deleted")
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
            else:
                return
                
                
               
                
                
                
                
    def reset_data(self): # Function for the "RESET" button, clears the left-side form
        self.ref_var.set("")
        self.cmpName_var.set("")
        self.typeMed_var.set("")
        self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.quantity_var.set("") # Added quantity
        
               
        
        
        
        
        
    def exit_app(self): # Function for the "EXIT" button
        mExit = messagebox.askyesno("Exit", "Do you want to exit the application?", parent=self.root)
        if mExit > 0:
            self.root.destroy()
            return
            
                        
                        
            
            
            
    def search_data(self): # Function for the "SEARCH" button
        search_col_map = { # Maps the user-friendly name to the database column name
            "Ref": "reg",
            "Medicine Name": "tabletname",
            "Lot": "lotno",
            "Quantity": "quantity" # Added quantity
        }
        db_col = search_col_map.get(self.search_by_var.get())

        if not db_col:
            messagebox.showerror("Error", "Invalid search criteria")
            return
            
        if self.search_txt_var.get() == "":
            messagebox.showerror("Error", "Search box is empty")
            return

        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysqlpassword1@",database="pharmacy")
            my_cursor=conn.cursor()
            
            query = f"SELECT * FROM pharmacy WHERE {db_col} LIKE %s" # Uses LIKE for partial matching
            search_val = ('%' + self.search_txt_var.get() + '%',)
            
            my_cursor.execute(query, search_val)
            rows = my_cursor.fetchall()
            
            self.pharmacy_table.delete(*self.pharmacy_table.get_children()) # Clears the table
            if rows:
                for i in rows:
                    self.pharmacy_table.insert("",END,values=i) # Inserts only the search results
            else:
                messagebox.showinfo("Not Found", "No records match your search")
                
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error during search: {err}")


if __name__=="__main__":    #This checks whether the file is being run directly or imported as a module.  When a Python file is executed directly, __name_ is set to "_main_".
                              #This ensures that the code inside this block only runs when the script is executed directly — not when imported.

    root=Tk()    #tkinter object created named "root". root is the name of our window
    obj=PharmacyManagementSystem(root)
    root.mainloop()    #makes the window open continously
