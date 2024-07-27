#import libraries
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#display_screen = tk.Tk()
#function to define database
def Database():
    global conn, cursor
    #creating stu_id database
    conn = sqlite3.connect("Book.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    #cursor.execute("CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, book_name TEXT, author_name TEXT, avail_issued TEXT, isbn_no TEXT, stu_id TEXT)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    global display_screen
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    # setting title for window
    display_screen.iconbitmap('icon_lib.ico')
    # setting icon for window
    display_screen.title("Book Managment Database")
    # display_screen.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called
    global tree
    global SEARCH
    global rid,book_name,author_name,isbn_no,issue_vol,avail_issued,stu_id,issue_date,return_date,book_condition
    SEARCH = StringVar()
    rid = StringVar()
    book_name = StringVar()
    author_name = StringVar()
    isbn_no = StringVar()
    issue_vol = StringVar()
    avail_issued = StringVar()
    stu_id = StringVar()
    issue_date = StringVar()
    return_date = StringVar()
    book_condition = StringVar()

    #creating frames for layout
    # topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    # first left frame for registration from
    LFrom = Frame(display_screen, width="850", bg="black")
    LFrom.pack(side=LEFT, fill=Y, ipadx=30)
    # seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=850, bg="black")
    LeftViewForm.pack(side=LEFT, fill=Y, ipadx=30)
    # mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=1100)
    MidViewForm.pack(fill=BOTH)
    # label for heading
    lbl_text = Label(TopViewForm, text="Book Managment System", font=('Times', 29), width=600, bg="grey")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="Book Name  ", font=("Arial", 11),bg="black",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arial",11,"bold"),textvariable=book_name).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Author Name ", font=("Arial", 11),bg="black",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"),textvariable=author_name).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="ISBN", font=("Arial", 11), bg="black", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"), textvariable=isbn_no).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Volume", font=("Arial", 11), bg="black", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"), textvariable=issue_vol).pack(side=TOP, padx=11, fill=X)

    Label(LFrom, text="Available or Issued", font=("Arial", 11),bg="black",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 11, "bold"),textvariable=avail_issued).pack(side=TOP, padx=11, fill=X)
    avail_issued.set("Select Available or Issued")
    content={'Available','Not available'}
    OptionMenu(LFrom,avail_issued,*content).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Student ID", font=("Arial", 11),bg="black",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"),textvariable=stu_id).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Issue Date", font=("Arial", 11), bg="black", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"), textvariable=issue_date).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Return Date", font=("Arial", 11), bg="black", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 11, "bold"), textvariable=return_date).pack(side=TOP, padx=11, fill=X)
    Label(LFrom, text="Condition of Book", font=("Arial", 11),bg="black",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 11, "bold"),textvariable=avail_issued).pack(side=TOP, padx=11, fill=X)
    book_condition.set("Condition")
    bcontent={'Good','Issue Found','Fine to be collected'}
    OptionMenu(LFrom, book_condition, *bcontent).pack(side=TOP, padx=11, fill=X)

    Button(LFrom,text="Submit",font=("Arial", 11, "bold"),command=register,bg="black",fg="white").pack(side=TOP, padx=11,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter Book Name to Search", font=('Times', 11),bg="black",fg='#ffffff')
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=11)
    search.pack(side=TOP, padx=11, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="black",fg='#ffffff')
    btn_search.pack(side=TOP, padx=11, pady=11, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="black",fg='#ffffff')
    btn_view.pack(side=TOP, padx=11, pady=11, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="black",fg='#ffffff')
    btn_reset.pack(side=TOP, padx=11, pady=11, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="black",fg='#ffffff')
    btn_delete.pack(side=TOP, padx=11, pady=11, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="black",fg='#ffffff')
    btn_delete.pack(side=TOP, padx=11, pady=11, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("rid", "book_name", "author_name", "isbn_no", "issue_vol","avail_issued","stu_id","issue_date","return_date","book_condition"),
                        selectmode="extended", height=110, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('rid', text="Book Id", anchor=W)
    tree.heading('book_name', text="Book Name", anchor=W)
    tree.heading('author_name', text="Author's Name", anchor=W)
    tree.heading('isbn_no', text="ISBN no", anchor=W)
    tree.heading('issue_vol', text="Volume", anchor=W)
    tree.heading('avail_issued', text="Available/Issued", anchor=W)
    tree.heading('stu_id', text="Student ID", anchor=W)
    tree.heading('issue_date', text="Date of Issue", anchor=W)
    tree.heading('return_date', text="Date of Return", anchor=W)
    tree.heading('book_condition', text="Book Condition", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=90)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()
    """if display_screen.quit():
        display_screen.protocol("WM_DELETE_WINDOW", on_closing)"""



#function to update data into database
def Update():
    Database()
    #getting form data
    book_name1=book_name.get()
    author_name1=author_name.get()
    avail_issued1=avail_issued.get()
    isbn_no1=isbn_no.get()
    stu_id1=stu_id.get()
    issue_date1=issue_date.get()
    return_date1=return_date.get()
    issue_vol1=issue_vol.get()
    book_condition1=book_condition.get()
    #applying empty validation
    if book_name1=='' or author_name1==''or avail_issued1=='' or isbn_no1==''or stu_id1=='' or return_date1==''or book_condition1==''or issue_vol1==''or issue_date1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE REGISTRATION SET book_name=?,author_name=?,avail_issued=?,isbn_no=?,stu_id=?,issue_date=?,issue_vol=?,book_condition=?,return_date=? WHERE RID = ?',(book_name1,author_name1,avail_issued1,isbn_no1,stu_id1,issue_date1,issue_vol1,book_condition1,return_date1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
        conn.close()

def register():
    Database()
    #getting form data
    book_name1=book_name.get()
    author_name1=author_name.get()
    avail_issued1=avail_issued.get()
    isbn_no1=isbn_no.get()
    stu_id1=stu_id.get()
    issue_date1=issue_date.get()
    return_date1=return_date.get()
    issue_vol1=issue_vol.get()
    book_condition1=book_condition.get()
    #applying empty validation
    if book_name1=='' or author_name1==''or avail_issued1=='' or isbn_no1==''or stu_id1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO REGISTRATION (book_name,author_name,avail_issued,isbn_no,stu_id,book_condition,issue_date,return_date, issue_vol)               VALUES (?,?,?,?,?,?,?,?,?)',(book_name1,author_name1,avail_issued1,isbn_no1,stu_id1,book_condition1,issue_date1,return_date1,issue_vol1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    book_name.set("")
    author_name.set("")
    isbn_no.set("")
    stu_id.set("")
    issue_date.set("")
    return_date.set("")
    issue_vol.set("")
    avail_issued.set("")
    book_condition.set("")
def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE book_name LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    #getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #set values in the fields
    book_name.set(selecteditem[1])
    author_name.set(selecteditem[2])
    avail_issued.set(selecteditem[5])
    isbn_no.set(selecteditem[3])
    issue_vol.set(selecteditem[4])
    stu_id.set(selecteditem[6])
    issue_date.set(selecteditem[7])
    return_date.set(selecteditem[8])
    book_condition.set(selecteditem[9])


"""def ask_quit():
    result1 = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                             icon="warning")
    if result1 == 'yes':
        display_screen = tk.Tk()
        display_screen.protocol("WM_DELETE_WINDOW", ask_quit)
        display_screen.destroy()"""


def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        display_screen.destroy()


#calling function
DisplayForm()
display_screen.protocol("WM_DELETE_WINDOW", on_closing)
if __name__=='__main__':
    #Running Application
    display_screen.mainloop()





