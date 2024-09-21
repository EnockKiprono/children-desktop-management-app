import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import mysql.connector as mysql
import os

window =tk.Tk()
window.title("Childrens home administration software")
window.geometry("1000x650")
window.configure(bg="purple")

from PIL import Image, ImageTk
image  = Image.open('children.jpeg')
image.thumbnail((50,50),Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=0, row=0)


Firstlabel = tk.Label(text = "CHILDRENS HOME ADMINISTRATION SOFTWARE",
foreground = "black",
background = "blue",
width = 40,
height = 2,
)
Firstlabel.grid(padx=5, pady=5, column=3, row=0)

frame1 = tk.Frame(padx=5, pady=5, bg='purple')
frame1.grid(column=1, row=1)

frame2 = tk.Frame(padx=5, pady=5, bg='purple')
frame2.grid(column=3, row=1)

con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
cursor = con.cursor()
cursor.execute("select postdesc from posts ORDER BY ID DESC LIMIT 1")
rows = cursor.fetchall()
i=6
for row in rows:
    for j in range(len(row)):
        info = tk.Text(frame2, width=80, fg='green', bg="black")
        info.grid(row=i, column=3)
        info.insert(tk.END, row[j])
        i=i+1


def cdatabase():
    cdatabase = tk.Toplevel()
    cdatabase.title("Children database administration")
    cdatabase.geometry("1000x650")
    cdatabase.columnconfigure(0, weight=40)
    cdatabase.configure(bg="purple")
    

    Firstlabel = tk.Label(text = "CHILDREN DATABASE ADMINISTRATION",
    width = 40,
    height = 2,
    foreground = 'black',
    master = cdatabase,
    bg='purple'
    )
    Firstlabel.grid(padx=5, pady=5, column=0, row=0)

    frame3 = tk.Frame(master=cdatabase, padx=5, pady=5, highlightbackground="green", highlightthickness=2, bg='purple')
    frame3.grid(column=0, row=1)

    
    def updatec():
        updatec = tk.Toplevel()
        updatec.title("Search child")
        updatec.geometry("1000x650")
        #updatec.columnconfigure(0, weight=1)
        #updatec.columnconfigure(1, weight=0)
        #updatec.columnconfigure(3, weight=2)
        updatec.configure(bg="purple")

        updateframe = tk.Frame(updatec, bg='purple', pady=140, highlightbackground="green", highlightthickness=2, height = 14)
        updateframe.grid(column=0, row=1, padx=60)

        frameoutputsearch = tk.Frame(master=updatec, bg='purple', padx=5, pady=50, highlightbackground="green", highlightthickness=2)
        frameoutputsearch.grid(column=1, row=1, padx=3)

        uplabel = tk.Label(text = "SEARCH/VIEW CHILD'S INFORMATION",
        width = 40,
        height = 2,
        foreground = 'black',
        master = updatec,
        bg='purple'
        )
        uplabel.grid(pady=5, row=0, column=0)

        namelabel = tk.Label(text = "Enter child's name:",
        foreground = "blue",
        bg='purple',
        width = 40,
        height = 2,
        master = updateframe
        )
        namelabel.grid()
        name = tk.Entry(master=updateframe, width=40)
        name.grid()

        infolabel = tk.Label(updatec, text="SEARCHED CHILD INFORMATION", bg='purple')
        infolabel.grid(row=0, column=1)

        ID = tk.Label(frameoutputsearch, text='ID', anchor='w', bg='green', width=15)
        ID.grid(pady=3, padx=3)
        parent_guardian = tk.Label(frameoutputsearch, text='parent/guardian', anchor='w', bg='green', width=15)
        parent_guardian.grid(pady=3, padx=3)
        child_name= tk.Label(frameoutputsearch, text='child_name', anchor='w', bg='green', width=15)
        child_name.grid(pady=3, padx=3)
        child_age = tk.Label(frameoutputsearch, text='child_age', anchor='w', bg='green', width=15)
        child_age.grid(pady=3, padx=3)
        date_of_birth = tk.Label(frameoutputsearch, text='date_of_birth', anchor='w', bg='green', width=15)
        date_of_birth.grid(pady=3, padx=3)
        gender = tk.Label(frameoutputsearch, text='gender', anchor='w', bg='green', width=15)
        gender.grid(pady=3, padx=3)
        guardian_contact = tk.Label(frameoutputsearch, text='guardian_contact', anchor='w', bg='green', width=15)
        guardian_contact.grid(pady=3, padx=3)
        location_address = tk.Label(frameoutputsearch, text='location/address', anchor='w', bg='green', width=15)
        location_address.grid(pady=3, padx=3)
        disbursement = tk.Label(frameoutputsearch, text='disbursement', anchor='w', bg='green', width=15)
        disbursement.grid(pady=3, padx=3)
        cc_number = tk.Label(frameoutputsearch, text='CC_number', anchor='w', bg='green', width=15)
        cc_number.grid(pady=3, padx=3)
        profile = tk.Label(frameoutputsearch, text='Profile picture', anchor='w', bg='green', width=15)
        profile.grid(pady=3, padx=3)

        date = tk.Label(frameoutputsearch, text='date_registered', anchor='w', bg='green', width=15)
        date.grid(pady=3, padx=3)

        def printfile():
            child_name = name.get()

            if(child_name == ""):
                mb.showinfo("Print to file status", "Name is required to print child's information")
            elif(child_name):
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("select * from childrenDatabase where child_name like '%{}%'".format(child_name))
                results = cursor.fetchall()
                if results:
                    newfile = open("SearchedChildInformation.txt","a+")
                    newfile.write('('+"\t"+'ID,'+"\t"+'Parent/guardian,'+"\t"+'Child_name,'+"\t"+"Child_age,"+"\t"+'Date_of_birth,'+"\t"+'gender,'+"\t"+'Guardian_contact,'+"\t"+'Location_address,'+"\t"+'disbursement,'+"\t"+'Credit_card_number,'+"\t"+'Profile_picture,'+"\t"+'Date_registered,'+"\t"+')'+"\t"+"\n")
                    newfile.write(str(results))
                    newfile.write("\n")
                    mb.showinfo("Printing to file status", "Successfully printed to SearchedChildInformation.txt file on the same folder.")
                    con.close()
                    newfile.close()

        printbtn = tk.Button(master=frameoutputsearch, text='PRINT TO FILE', fg='green', bg='cyan', command=printfile, width = 10, height = 1)
        printbtn.grid(pady=3)

        def search():
            #search = tk.Toplevel()
            #search.title("Child information")
            #search.geometry("1000x650")
            child_name = name.get()

            if(child_name == ""):
                mb.showinfo("Search status", "Name is required to search a child")
            
            elif(child_name):
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("select * from childrenDatabase where child_name like '%{}%'".format(child_name))
                rows = cursor.fetchall()
                i=2
                for row in rows:
                    for j in range(len(row)):
                        info = tk.Entry(frameoutputsearch, width=30, fg='blue')
                        info.grid(row=j, column=i, pady=3, padx=3)
                        info.insert(tk.END, row[j])
       
                    i=i+1

                    print("child_name = ", row[1])
                    print("child_age = ", row[2])
                    print("date_of_birth = ", row[3])
                    print("gender = ", row[4])
                    print("guardian_contact = ", row[5])
                    print("location_address = ", row[6])
                    print("disbursement = ", row[7])
                    print("location = ", row[8])
                    print("cc_number = ", row[9])
                    print("date = ", row[10])
            else:
                mb.showinfo("Search status", "Child not found")
                con.close()
                

        submitbtn = tk.Button(
        text = "SEARCH",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=updateframe, command=search
        )
        submitbtn.grid(pady=3)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=updateframe, command=updatec.destroy
        )
        logoutbutton.grid(pady=10)

    viewbutton = tk.Button(
    text = "Search/view child",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2,
    master=frame3,
    command=updatec
    )
    viewbutton.grid(pady=3)

    def registerchild():
        registerchild = tk.Toplevel()
        registerchild.title("Children registration")
        registerchild.geometry("1000x800")
        registerchild.configure(bg="purple")
        #registerchild.columnconfigure(0, weight=5)

        Firstlabel = tk.Label(text = "CHILDREN REGISTRATION",
        
        width = 40,
        height = 2,
        bg='purple',
        foreground = 'black',
        master = registerchild
        )
        Firstlabel.grid(column=0, row=0)

        uploframe = tk.Frame(master=registerchild, padx=5, pady=5, highlightbackground="green", highlightthickness=2, bg='purple')
        uploframe.grid(column=1, row=1)
        uploadframe = tk.Frame(master=registerchild, padx=5, pady=5, highlightbackground="green", highlightthickness=2, bg='purple')
        uploadframe.grid(padx=3, column=0, row=1)
        regframe = tk.Frame(master=registerchild, padx=5, pady=5, highlightbackground="green", highlightthickness=2, bg='purple')
        regframe.grid(pady=1, column=0, row=2)
       
        global filename

        def upload_profile():
            global filename, img
            file_types = [('Jpg files','*.jpg'),('Png files','*.png'),('Jpeg files','*.jpeg')]
            filename = fd.askopenfilename(parent=registerchild, filetypes=file_types)
            img=Image.open(filename)
            Img_resized=img.resize((500,500))
            img = ImageTk.PhotoImage(Img_resized)
            profileuplo = tk.Button(uploframe, image=img)
            profileuplo.grid(pady=5, columnspan=1, rowspan=2)

        uploadedlabel = tk.Label(text = "CHOSEN PROFILE PICTURE FOR UPLOAD",
        foreground = "black",
        width = 40,
        height = 2,
        bg='purple',
        master=uploframe
        )
        uploadedlabel.grid()
        
        namelabel = tk.Label(text = "Parent/Guardian name:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        namelabel.grid()
        parent = tk.Entry(master=uploadframe, width=40)
        parent.grid()


        namelabel = tk.Label(text = "Childs name:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        namelabel.grid()
        name = tk.Entry(master=uploadframe, width=40)
        name.grid()


        agelabel = tk.Label(text = "Childs age:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        agelabel.grid()
        age = tk.Entry(master=uploadframe, width=40)
        age.grid()


        doblabel = tk.Label(text = "Date of birth:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        doblabel.grid()
        dob = tk.Entry(master=uploadframe, width=40)
        dob.grid()


        genderlabel = tk.Label(text = "Gender:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        genderlabel.grid()
        genders = tk.Entry(master=uploadframe, width=40)
        genders.grid()

        contactlabel = tk.Label(text = "Guardian contact:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        contactlabel.grid()
        contact = tk.Entry(master=uploadframe, width=40)
        contact.grid()

        locationlabel = tk.Label(text = "Location/Address:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        locationlabel.grid()
        location = tk.Entry(master=uploadframe, width=40)
        location.grid()

        disbursementlabel = tk.Label(text = "Disbursement:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        disbursementlabel.grid()
        disbursements = tk.Entry(master=uploadframe, width=40)
        disbursements.grid()

        cclabel = tk.Label(text = "Credit card number:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=uploadframe
        )
        cclabel.grid()
        creditcard = tk.Entry(master=uploadframe, width=40)
        creditcard.grid()

        profile = tk.Button(uploadframe, bg='yellow', fg='green', text='Choose childs profile picture', command=lambda:upload_profile())
        profile.grid(pady=1)

        def insert():
            parent_guardian = parent.get()
            child_name = name.get()
            child_age = age.get()
            date_of_birth = dob.get()
            gender = genders.get()
            guardian_contact = contact.get()
            location_address = location.get()
            disbursement = disbursements.get()
            cc_number = creditcard.get()

            profilephoto = filename

            if(parent_guardian == "" or name == "" or age == "" or dob == "" or genders == "" or contact == "" or location == "" or disbursements == "" or creditcard == ""):
                mb.showinfo("Registration status", "Please enter all the required fields")
            else:
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("insert into childrenDatabase (parent_guardian, child_name, child_age, date_of_birth, gender, guardian_contact, location_address, disbursement, cc_number, profile, date) values ('" +parent_guardian+ "', '" +child_name+ "', '" +child_age+ "', '" +date_of_birth+ "', '" +gender+ "', '" +guardian_contact+ "', '" +location_address+ "', '" +disbursement+ "', '" +cc_number+ "', '" +profilephoto+ "', NOW())")
                cursor.execute("commit")
  
                mb.showinfo("Registration status", "Successfully registered the child")
                con.close()

        submitbtn = tk.Button(
        text = "REGISTER",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=regframe, command=insert
        )
        submitbtn.grid(padx=5)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=regframe, command=registerchild.destroy
        )
        logoutbutton.grid(column=1, row=0)
        
        registerchild.grid()



        
    addbutton = tk.Button(
    text = "Register new child",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame3, command=registerchild
    )
    addbutton.grid(pady=3)



    def deleteui():
        deleteui = tk.Toplevel()
        deleteui.title("Delete a child from the database")
        deleteui.geometry("1000x650")
        deleteui.columnconfigure(3, weight=80)
        deleteui.configure(bg="purple")
        
        deleteframe = tk.Frame(deleteui, highlightbackground="green", highlightthickness=2, bg='purple')
        deleteframe.grid(row=0, column=3)
        removelabel = tk.Label(text = "Delete a child from the database",
        
        width = 40,
        height = 2,
        foreground = 'black',
        master = deleteframe,
        bg='purple'
        )
        removelabel.grid(padx=5, pady=5, column=3, row=0)

        enternamelabel = tk.Label(text = "Full name:",
        foreground = "blue",
        width = 40,
        height = 2,
        master=deleteframe,
        bg='purple'
        )
        enternamelabel.grid(column=3, row=1)
        name = tk.Entry(master=deleteframe, width=40)
        name.grid(column=3, row=2, pady=3)

        def zdel():
            if(name.get() == ""):
                mb.showinfo("Child deletion status", "Please enter the name of the child to delete from the database")
            else:
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("delete from childrenDatabase where child_name='"+ name.get() +"'")
                cursor.execute("commit")
  
                name.delete(0, 'end')
                mb.showinfo("Successfully deleted from children database")
                con.close()

        submitnamebtn = tk.Button(
        text = "DELETE",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=deleteframe, command=zdel
        )
        submitnamebtn.grid(column=3, row=5, pady=3)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=deleteframe, command=deleteui.destroy
        )
        logoutbutton.grid(column=3, row=6, pady=3)

    removebutton = tk.Button(
    text = "Delete child",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame3, command=deleteui
    )
    removebutton.grid(pady=3)

    def edit():
        edit = tk.Toplevel()
        edit.title("Edit a child's information")
        edit.geometry("1000x800")
        edit.configure(bg='purple')
        

        Firstlabel = tk.Label(text = "EDIT A CHILD'S INFORMATION",
        
        width = 40,
        height = 2,
        foreground = 'black',
        bg='purple',
        master = edit,

        )
        Firstlabel.grid(padx=5, pady=5, column=0, row=0)

        namelabel = tk.Label(text = "Parent/Guardian name:",
        foreground = "blue",
        bg='purple',
        width = 40,
        height = 2,
        master=edit
        )
        namelabel.grid()
        parent = tk.Entry(master=edit, width=40)
        parent.grid()


        namelabel = tk.Label(text = "Childs name:",
        foreground = "blue",
        width = 40,
        height = 2,
        bg='purple',
        master=edit
        )
        namelabel.grid()
        name = tk.Entry(master=edit, width=40)
        name.grid()


        agelabel = tk.Label(text = "Childs age:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        agelabel.grid()
        age = tk.Entry(master=edit, width=40)
        age.grid()


        doblabel = tk.Label(text = "Date of birth:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        doblabel.grid()
        dob = tk.Entry(master=edit, width=40)
        dob.grid()


        genderlabel = tk.Label(text = "Gender:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        genderlabel.grid()
        genders = tk.Entry(master=edit, width=40)
        genders.grid()

        contactlabel = tk.Label(text = "Guardian contact:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        contactlabel.grid()
        contact = tk.Entry(master=edit, width=40)
        contact.grid()

        locationlabel = tk.Label(text = "Location/Address:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        locationlabel.grid()
        location = tk.Entry(master=edit, width=40)
        location.grid()

        disbursementlabel = tk.Label(text = "Disbursement:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        disbursementlabel.grid()
        disbursements = tk.Entry(master=edit, width=40)
        disbursements.grid()

        cclabel = tk.Label(text = "Credit card number:",
        foreground = "blue",
        width = 40,
        bg='purple',
        height = 2,
        master=edit
        )
        cclabel.grid()
        creditcard = tk.Entry(master=edit, width=40)
        creditcard.grid()

        def editinfo():
            parent_guardian = parent.get()
            child_name = name.get()
            child_age = age.get()
            date_of_birth = dob.get()
            gender = genders.get()
            guardian_contact = contact.get()
            location_address = location.get()
            disbursement = disbursements.get()
            cc_number = creditcard.get()

            if(parent_guardian == "" or name == "" or age == "" or dob == "" or genders == "" or contact == "" or location == "" or disbursements == "" or creditcard == ""):
                mb.showinfo("Edit status", "Please enter all the required fields")
            else:
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("insert into childrenDatabase (parent_guardian, child_name, child_age, date_of_birth, gender, guardian_contact, location_address, disbursement, cc_number, date) values ('" +parent_guardian+ "', '" +child_name+ "', '" +child_age+ "', '" +date_of_birth+ "', '" +gender+ "', '" +guardian_contact+ "', '" +location_address+ "', '" +disbursement+ "', '" +cc_number+ "', NOW())")
                cursor.execute("commit")
  
                mb.showinfo("Status", "Successfully edited the child")
                con.close()


        submitbtn = tk.Button(
        text = "EDIT",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=edit, command=editinfo
        )
        submitbtn.grid(pady=10, padx=500)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=edit, command=edit.destroy
        )
        logoutbutton.grid(pady=3)

    editbutton = tk.Button(
    text = "Edit child's information",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame3, command=edit
    )
    editbutton.grid(pady=3)

    def allui():
        allui = tk.Toplevel()
        allui.title("All children data")
        allui.geometry("1200x1200")
        #allui.columnconfigure(0, weight=40)
        allui.configure(bg="purple")

        frameallui = tk.Frame(allui, padx=5, pady=5, bg='purple')
        frameallui.grid(column=0, row=0)

        Firstlabel = tk.Label(text = "ALL CHILDREN DATA",
        
        width = 40,
        height = 2,
        foreground = 'blue',
        master = frameallui,
        bg='purple'
        )
        Firstlabel.grid()

        #all children should appear here
        all = tk.Text(
        foreground = "green",
        background = "black",
        width = 150,
        #height = 50,
        master=frameallui
        )
        all.grid()

        def printalltofile():
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("select * from childrenDatabase")
                results = cursor.fetchall()
                if results:
                    newfile = open("AllChildren.txt","a+")
                    newfile.write('('+"\t"+'ID,'+"\t"+'Parent/guardian,'+"\t"+'Child_name,'+"\t"+"Child_age,"+"\t"+'Date_of_birth,'+"\t"+'gender,'+"\t"+'Guardian_contact,'+"\t"+'Location_address,'+"\t"+'disbursement,'+"\t"+'Credit_card_number,'+"\t"+'Profile_picture,'+"\t"+'Date_registered,'+"\t"+')'+"\t"+"\n")
                    newfile.write(str(results))
                    newfile.write("\n")
                    mb.showinfo("Printing to file status", "Successfully printed to AllChildren.txt file on the same folder.")
                    con.close()
                    newfile.close()

        printbtn = tk.Button(master=frameallui, text='PRINT TO FILE', fg='green', bg='cyan', command=printalltofile, width = 10, height = 1)
        printbtn.grid(pady=3)

        con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
        cursor = con.cursor()
        cursor.execute("select * from childrenDatabase")
        rows = cursor.fetchall()
        i=0
        for row in rows:
            for j in range(len(row)):
                info = tk.Entry(all, width=10, fg='blue')
                info.grid(row=i, column=j)
                info.insert(tk.END, row[j])
                i=i+1

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=frameallui, command=allui.destroy
        )
        logoutbutton.grid(pady=3)


    listallbutton = tk.Button(
    text = "List all children",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame3, command=allui
    )
    listallbutton.grid(pady=3)

    logoutbutton = tk.Button(
    text = "EXIT",
    foreground = "red",
    background = "cyan",
    width = 10,
    height = 1, master=frame3, command=cdatabase.destroy
    )
    logoutbutton.grid(pady=3)


databutton = tk.Button(
text = "Children database administration",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1, command=cdatabase
)
databutton.grid(pady=3)


def filess():
    filess = tk.Toplevel()
    filess.title("Manage files")
    filess.geometry("1000x650")
    filess.columnconfigure(0, weight=40)
    filess.configure(bg="purple")

    frame5 = tk.Frame(master=filess, padx=5, pady=5, bg='purple')
    frame6 = tk.Frame(padx=5, pady=5)


    Firstlabel = tk.Label(text = "MANAGE ALL COMPUTER FILES",
    width = 40,
    height = 2,
    foreground = 'black',
    bg='purple',
    master = frame5
    )
    Firstlabel.grid()

    def openFolder():
        the_folder = fd.askdirectory(title = "Select Folder to open")  
        os.startfile(the_folder)

    openbutton = tk.Button(
    text = "Open a folder",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=openFolder
    )
    openbutton.grid(pady=3)

    def deleteFolder():
        folderToDelete = fd.askdirectory(title = 'Select a folder to delete')  
        os.rmdir(folderToDelete)  
        mb.showinfo("The selected folder has been deleted!")  

    deletebutton = tk.Button(
    text = "Delete a folder",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=deleteFolder
    )
    deletebutton.grid(pady=3)

    def openFile():
        the_file = fd.askopenfilename(title = "Select a file of any type",  
        filetypes = [("All files", "*.*")]  
        )  
        os.startfile(os.path.abspath(the_file))

    openfilebutton = tk.Button(
    text = "Open a file",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=openFile
    )
    openfilebutton.grid(pady=3)

    def deleteFile():
        the_file = fd.askopenfilename(  
        title = "Choose a file to delete",  
        filetypes = [("All files", "*.*")]  
        )  
        os.remove(os.path.abspath(the_file))  
        mb.showinfo(title = "File deleted!", message = "The selected file has been deleted.")

    deletefilebutton = tk.Button(
    text = "Delete a file",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=deleteFile
    )
    deletefilebutton.grid(pady=3)

    def copyFile():
        fileToCopy = fd.askopenfilename(  
        title = "Select a file to copy",  
        filetypes=[("All files", "*.*")]  
        )
        directoryToPaste = fd.askdirectory(title = "Select the folder to paste the file")
        try:
            shutil.copy(fileToCopy, directoryToPaste)  
            mb.showinfo(  
            title = "File copied!",  
            message = "The selected file has been copied to the selected location."  
            )  
        except:
            mb.showerror(  
            title = "Error!",  
            
            message = "Selected file is unable to copy to the selected location. Please try again!"  
            )

    copyfilebutton = tk.Button(
    text = "Copy a file",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=copyFile
    )
    copyfilebutton.grid(pady=3)

    def moveFolder():
        folderToMove = fd.askdirectory(title = 'Select the folder you want to move')  
        mb.showinfo(message = 'Folder has been selected to move. Now, select the desired destination.')  
        des = fd.askdirectory(title = 'Destination')  
  
        try:
            shutil.move(folderToMove, des)  
            mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')  
        except:  
            mb.showerror('Error!', 'The Folder cannot be moved. Make sure that the destination exists')

    movebutton = tk.Button(
    text = "Move a folder",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=frame5, command=moveFolder
    )
    movebutton.grid(pady=3)

    logoutbutton = tk.Button(
    text = "EXIT",
    foreground = "red",
    background = "cyan",
    width = 10,
    height = 1, master=frame5, command=filess.destroy
    )
    logoutbutton.grid(pady=3)


    frame5.grid(column=0, row=0)
    frame6.grid(column=3, row=2)



filesbutton = tk.Button(
text = "Manage computer files",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1,
command=filess,
borderwidth=0
)
filesbutton.grid(pady=3)


def administer():
    administer = tk.Toplevel()
    administer.title("Admin database administration")
    administer.geometry("1000x650")
    administer.configure(bg="purple")

    Firstlabel = tk.Label(text = "ADMIN DATABASE ADMINISTRATION",
    width = 40,
    height = 2,
    foreground = 'black',
    master = administer,
    bg='purple'
    )
    Firstlabel.grid(padx=5, pady=5, column=0, row=0)



    framenine = tk.Frame(master=administer, padx=5, pady=5)
    frame10 = tk.Frame(padx=5, pady=5)

    def allusers():
        allusers = tk.Toplevel()
        allusers.title("Software users")
        allusers.geometry("1000x650")
        allusers.columnconfigure(0, weight=40)
        allusers.configure(bg="purple")

        frameallusers = tk.Frame(allusers, padx=5, pady=5, bg='black')
        frameallusers.grid(column=0, row=0)

        Firstlabel = tk.Label(text = "SOFTWARE USERS",
        
        width = 40,
        height = 2,
        foreground = 'black',
        bg='purple',
        master = frameallusers
        )
        Firstlabel.grid()

        #all USERS should appear here
        users = tk.Text(
        foreground = "green",
        background = "black",
        width = 90,
        height = 20, master=frameallusers
        )
        users.grid(pady=3)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=frameallusers, command=allusers.destroy
        )
        logoutbutton.grid(pady=20)

    viewbutton = tk.Button(
    text = "View users",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=allusers
    )
    viewbutton.grid(pady=3)



    def addusers():
        addusers = tk.Toplevel()
        addusers.title("Add new users")
        addusers.geometry("1000x650")
        addusers.columnconfigure(0, weight=40)
        addusers.configure(bg="purple")
        
        addusersframe = tk.Frame(addusers, highlightbackground="green", bg='purple', highlightthickness=2)
        addusersframe.grid(row=0, column=0, padx=20, pady=20)
        addlabel = tk.Label(text = "ADD NEW USER",
        
        width = 20,
        height = 2,
        foreground = 'blue',
        master = addusersframe,
        bg='purple'
        )
        addlabel.grid(pady=5)

        enternamelabel = tk.Label(text = "Username:",
        foreground = "green",
        width = 20,
        height = 2,
        master=addusersframe,
        bg='purple'
        )
        enternamelabel.grid()
        username = tk.Entry(master=addusersframe, width=20)
        username.grid(pady=5)

        enterpasswordlabel = tk.Label(text = "Password:",
        foreground = "green",
        width = 40,
        height = 2,
        master=addusersframe,
        bg='purple'
        )
        enterpasswordlabel.grid()
        userpass = tk.Entry(master=addusersframe, width=20)
        userpass.grid(pady=5)

        def addus():
            user = username.get()
            password = userpass.get()

            con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
            cursor = con.cursor()
            cursor.execute("insert into users (username, password, date) values ('" +user+ "', '" +password+ "', NOW())")
            cursor.execute("commit")
  
            username.delete(0, 'end')
            mb.showinfo("Successfully added the user")
            con.close()

        submitusersbtn = tk.Button(
        text = "ADD",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=addusersframe, command=addus
        )
        submitusersbtn.grid(pady=5)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=addusersframe, command=addusers.destroy
        )
        logoutbutton.grid(pady=20)

    addbutton = tk.Button(
    text = "Add users",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=addusers
    )
    addbutton.grid(padx=400, pady=3)

    def deleteusers():
        deleteusers = tk.Toplevel()
        deleteusers.title("Delete database users")
        deleteusers.geometry("1000x650")
        deleteusers.columnconfigure(0, weight=40)
        deleteusers.configure(bg="purple")
        
        deleteusersframe = tk.Frame(deleteusers, highlightbackground="green", highlightthickness=2, bg='purple')
        deleteusersframe.grid(row=0, column=0, padx=40, pady=20)
        deletelabel = tk.Label(text = "DELETE USER",
        
        width = 20,
        height = 1,
        foreground = 'black',
        bg='purple',
        master = deleteusersframe
        )
        deletelabel.grid(pady=3)

        enternamelabel = tk.Label(text = "Username:",
        foreground = "green",
        width = 20,
        height = 1,
        master=deleteusersframe,
        bg='purple'
        )
        enternamelabel.grid(pady=3)
        username = tk.Entry(master=deleteusersframe, width=20)
        username.grid(pady=3)

        enterIDlabel = tk.Label(text = "Database ID:",
        foreground = "green",
        width = 20,
        height = 1,
        master=deleteusersframe,
        bg='purple'
        )
        enterIDlabel.grid(pady=3)
        IDs = tk.Entry(master=deleteusersframe, width=20)
        IDs.grid(pady=3)

        def deleteus():
            user = username.get()
            IDss = IDs.get()

            con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
            cursor = con.cursor()
            cursor.execute("delete from users where username='" +user+ "' AND ID='" +IDss+ "'")
            cursor.execute("commit")
  
            username.delete(0, 'end')
            mb.showinfo("User deletion status", "Successfully deleted the user")
            con.close()

        submitusersbtn = tk.Button(
        text = "DELETE USER",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=deleteusersframe, command=deleteus
        )
        submitusersbtn.grid()

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=deleteusersframe, command=deleteusers.destroy
        )
        logoutbutton.grid(pady=20)

    deleteusersbutton = tk.Button(
    text = "Delete users",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=deleteusers
    )
    deleteusersbutton.grid(pady=3)

    def showtables():
        showtables = tk.Toplevel()
        showtables.title("Database tables")
        showtables.geometry("1000x650")
        showtables.columnconfigure(0, weight=40)
        showtables.configure(bg="purple")

        frametables = tk.Frame(showtables, padx=5, pady=5, bg='black')
        frametables.grid(column=0, row=0)

        Firstlabel = tk.Label(text = "TABLES CONTAINING CHILDREN DATA",
        
        width = 40,
        height = 2,
        foreground = 'black',
        bg='purple',
        master = frametables
        )
        Firstlabel.grid()

        tables = tk.Text(
        foreground = "green",
        background = "black",
        width = 90,
        height = 20, master=frametables
        )
        tables.grid(pady=3)

        def show():
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("SELECT table_name from information_schema.tables")
                rows = cursor.fetchall()
                i=0
                for row in rows:
                    for j in range(len(row)):
                        info = tk.Entry(tables, width=30, fg='blue')
                        info.grid(row=j, column=i, pady=3, padx=3)
                        info.insert(tk.END, row[j])
                    i=i+1
    
                mb.showinfo("Search status", "Child not found")
                con.close()

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=frametables, command=showtables.destroy
        )
        logoutbutton.grid(pady=20)

    showtables = tk.Button(
    text = "Show tables",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=showtables
    )
    showtables.grid(pady=3)

    def contents():
        contents = tk.Toplevel()
        contents.title("Database tables")
        contents.geometry("1000x650")
        contents.columnconfigure(0, weight=40)
        contents.configure(bg="purple")

        frametables = tk.Frame(contents, padx=5, pady=5, bg='black')
        frametables.grid(column=0, row=0)

        Firstlabel = tk.Label(text = "VIEW TABLE CONTENTS",
        
        width = 40,
        height = 1,
        foreground = 'blue',
        bg='black',
        master = frametables
        )
        Firstlabel.grid(pady=10)

        contentlabel = tk.Label(text = "Table name:",
        foreground = "green",
        width = 20,
        bg='black',
        height = 2,
        master=frametables
        )
        contentlabel.grid(pady=3)
        table = tk.Entry(master=frametables, width=30)
        table.grid(pady=3)

        def showtabledata():
                showtabledata = tk.Toplevel()
                showtabledata.title("Table data")
                showtabledata.geometry("1000x650")
                showtabledata.configure(bg="purple")
                showtabledata.columnconfigure(0, weight=5)

                tlabel = tk.Label(text = "TABLE DATA",
        
                width = 40,
                height = 2,
                foreground = 'black',
                master = showtabledata,
                bg='purple'
                )
                tlabel.grid(pady=3, column=0, row=0)

                exitbutton = tk.Button(
                text = "EXIT",
                foreground = "red",
                background = "cyan",
                width = 10,
                height = 1, master=showtabledata, command=showtabledata.destroy
                )
                exitbutton.grid(pady=20, column=0, row=1)

                tables = tk.Text(
                foreground = "green",
                background = "black",
                width = 130,
                height = 40, master=showtabledata
                )
                tables.grid(column=0, row=2, pady=5)

                tables = table.get()
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("select * from {}".format(tables))
                rows = cursor.fetchall()
                i=0
                for row in rows:
                    for j in range(len(row)):
                        info = tk.Entry(tables, width=30, fg='blue')
                        info.grid(row=j, column=i, pady=3, padx=3)
                        info.insert(tk.END, row[j])
                    i=i+1
                con.close()

        stables = tk.Button(
        text = "VIEW TABLE DATA",
        foreground = "green",
        background = "cyan",
        width = 15,
        height = 1, master=frametables, command=showtabledata
        )
        stables.grid(pady=5)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=frametables, command=contents.destroy
        )
        logoutbutton.grid(pady=20)

    showtables = tk.Button(
    text = "Show table data",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=contents
    )
    showtables.grid(pady=3)

    def changepassword():
        changepassword = tk.Toplevel()
        changepassword.title("Change admin password")
        changepassword.geometry("1000x650")
        changepassword.columnconfigure(0, weight=40)
        changepassword.configure(bg="purple")
        
        changepassframe = tk.Frame(changepassword, highlightbackground="green", highlightthickness=2, bg='purple')
        changepassframe.grid(row=0, column=0, padx=20, pady=20)
        passlabel = tk.Label(text = "CHANGE ADMIN PASSWORD",
        
        width = 40,
        height = 2,
        foreground = 'black',
        master = changepassframe,
        bg='purple'
        )
        passlabel.grid(pady=3)

        usernamelb = tk.Label(text = "Admin username:",
        foreground = "green",
        width = 20,
        bg='purple',
        height = 2,
        master=changepassframe
        )
        usernamelb.grid(pady=3)
        username = tk.Entry(master=changepassframe, width=20)
        username.grid(pady=3)

        enternewlabel = tk.Label(text = "New password:",
        foreground = "green",
        width = 20,
        bg='purple',
        height = 2,
        master=changepassframe
        )
        enternewlabel.grid(pady=3)
        passw = tk.Entry(master=changepassframe, width=20)
        passw.grid(pady=3)

        def passchange():
                ps = passw.get()
                us = username.get()
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("UPDATE admin SET password=('"+ ps +"') where username=('"+ us +"')")
                cursor.execute("commit")
                mb.showinfo("Admin password change status", "Admin password successfully changed")
                con.close()

        submitusersbtn = tk.Button(
        text = "CHANGE",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=changepassframe,
        command=passchange
        )
        submitusersbtn.grid(pady=3)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=changepassframe, command=changepassword.destroy
        )
        logoutbutton.grid(pady=20)


    changepassbutton = tk.Button(
    text = "Change admin password",
    foreground = "green",
    background = "cyan",
    width = 20,
    height = 2, master=administer, command=changepassword
    )
    changepassbutton.grid(pady=3)

    logoutbutton = tk.Button(
    text = "EXIT",
    foreground = "red",
    background = "cyan",
    width = 10,
    height = 1, master=administer, command=administer.destroy
    )
    logoutbutton.grid(pady=3)

adminbutton = tk.Button(
text = "Database administration",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1, command=administer
)

adminbutton.grid(pady=3)

def post():
    post = tk.Toplevel()
    post.title("Post description")
    post.geometry("1000x650")
    post.columnconfigure(4, weight=40)
    post.configure(bg="purple")

    Firstlabel = tk.Label(text = "POST HOME WINDOW DESCRIPTION",
    width = 40,
    height = 2,
    foreground = 'black',
    master = post,
    bg='purple'
    )
    Firstlabel.grid(column=4, row=1)

    description = tk.Entry(master=post)
    description.grid(column=4, row=3, ipadx=150, ipady=90)

    def postdescription():
        postdesc = description.get()
        if (postdesc == ""):
            mb.showinfo("Post status", "Couldn't post, please enter the description")
        
        else:
            con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
            cursor = con.cursor()
            cursor.execute("insert into posts (postdesc, date) values ('" +postdesc+ "', NOW())")
            cursor.execute("commit")
  
            mb.showinfo("Post status", "Successfully posted the description at the parent window")
            con.close()

    postdecbutton = tk.Button(
    text = "POST",
    foreground = "green",
    background = "cyan",
    width = 10,
    height = 1, master=post, command=postdescription
    )
    postdecbutton.grid(column=4, row=4, pady=3)

    logoutbutton = tk.Button(
    text = "EXIT",
    foreground = "red",
    background = "cyan",
    width = 10,
    height = 1, master=post, command=post.destroy
    )
    logoutbutton.grid(pady=6, column=4, row=5)

contentbutton = tk.Button(
text = "Post content",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1, command=post
)

contentbutton.grid(pady=3)

def customize():
    customize = tk.Toplevel()
    customize.title("Customization")
    customize.geometry("1000x650")
    customize.columnconfigure(0, weight=40)
    customize.configure(bg="purple")

    Firstlabel = tk.Label(text = "MAIN WINDOW INTERFACE CUSTOMIZATION",
    width = 40,
    height = 2,
    foreground = 'black',
    master = customize,
    bg='purple'
    )
    Firstlabel.grid(pady=3, column=0, row=0)

    def custolight():
        window.configure(bg="white")

    cust = tk.Button(
    text = "Light mode",
    foreground = "green",
    background = "white",
    width = 35,
    height = 2,
    master=customize,
    command=custolight
    )
    cust.grid(pady=3, column=0, row=1)

    def custodark():
        window.configure(bg="black")

    custdark = tk.Button(
    text = "Dark mode",
    foreground = "green",
    background = "black",
    width = 35,
    height = 2,
    master=customize,
    command=custodark
    )
    custdark.grid(pady=3, column=0, row=2)

    logoutbutton = tk.Button(
    text = "EXIT",
    foreground = "red",
    background = "cyan",
    width = 25,
    height = 2, master=customize, command=customize.destroy
    )
    logoutbutton.grid(pady=3, column=0, row=3)

    customize.mainloop()



custbutton = tk.Button(
text = "Customization",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1,
command=customize
)
custbutton.grid(pady=3)

def login():
        login = tk.Toplevel()
        login.title("ADMIN")
        login.geometry("1000x650")
        login.columnconfigure(0, weight=40)
        login.configure(bg="purple")
        
        logframe = tk.Frame(login, highlightbackground="green", highlightthickness=2, bg='purple')
        logframe.grid(row=0, column=0, padx=20, pady=20)
        loglabel = tk.Label(text = "ADMIN REGISTRATION",
        
        width = 40,
        height = 2,
        foreground = 'black',
        master = logframe,
        bg='purple'
        )
        loglabel.grid(pady=3)

        usernamelb = tk.Label(text = "Username:",
        foreground = "green",
        width = 20,
        bg='purple',
        height = 2,
        master=logframe
        )
        usernamelb.grid(pady=3)
        username = tk.Entry(master=logframe, width=20)
        username.grid(pady=3)

        passlabel = tk.Label(text = "Password:",
        foreground = "green",
        width = 20,
        bg='purple',
        height = 2,
        master=logframe
        )
        passlabel.grid(pady=3)
        passw = tk.Entry(master=logframe, width=20)
        passw.grid(pady=3)

        def registeradmin():
                ps = passw.get()
                us = username.get()

                #if (ps == "", us == ""):
                    #mb.showinfo("Admin registration status", "Enter name or password")
                #else:
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("insert into admin (username, password) values ('" +us+ "', '" +ps+ "')")
                cursor.execute("commit")
                mb.showinfo("Registration status", "Admin registered successfully")
                con.close()

        submitbtn = tk.Button(
        text = "REGISTER",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=logframe,
        command=registeradmin
        )
        submitbtn.grid(pady=3)

        notlabel = tk.Label(text = "Already registered?",
        foreground = "green",
        width = 20,
        bg='purple',
        height = 2,
        master=logframe
        )
        notlabel.grid(pady=3)

        def loginadmin():
            loginadmin = tk.Toplevel()
            loginadmin.title("ADMIN")
            loginadmin.geometry("1000x650")
            loginadmin.columnconfigure(0, weight=40)
            loginadmin.configure(bg="purple")
        
            logfra = tk.Frame(loginadmin, highlightbackground="green", highlightthickness=2, bg='purple')
            logfra.grid(row=0, column=0, padx=20, pady=20)
            loglabel = tk.Label(text = "ADMIN LOGIN",
        
            width = 40,
            height = 2,
            foreground = 'black',
            master = logfra,
            bg='purple'
            )
            loglabel.grid(pady=3)

            usernamelb = tk.Label(text = "Username:",
            foreground = "green",
            width = 20,
            bg='purple',
            height = 2,
            master=logfra
            )
            usernamelb.grid(pady=3)
            username = tk.Entry(master=logfra, width=20)
            username.grid(pady=3)

            passlabel = tk.Label(text = "Password:",
            foreground = "green",
            width = 20,
            bg='purple',
            height = 2,
            master=logfra
            )
            passlabel.grid(pady=3)
            passw = tk.Entry(master=logfra, width=20)
            passw.grid(pady=3)

            def loginadmini():
                ps = passw.get()
                us = username.get()

                #if (ps == "", us == ""):
                    #mb.showinfo("Admin login status", "Enter name or password")
                #else:
                con = mysql.connect(host="localhost", user="root", password="emmy", database="children")
                cursor = con.cursor()
                cursor.execute("select username, password from admin where username='" +us+ "' and password='" +ps+ "')")
                cursor.execute("commit")
                mb.showinfo("Registration status", "Admin login successfully")
                con.close()
            
            submitbtn = tk.Button(
            text = "LOGIN",
            foreground = "green",
            background = "cyan",
            width = 10,
            height = 1, master=logfra,
            command=loginadmini
            )
            submitbtn.grid(pady=3)

            notlabel = tk.Label(text = "Not yet registered?",
            foreground = "green",
            width = 20,
            bg='purple',
            height = 2,
            master=logfra
            )
            notlabel.grid(pady=3)

            regbutton = tk.Button(
            text = "REGISTER",
            foreground = "green",
            background = "cyan",
            width = 10,
            height = 1, master=logfra,
            command=login
            )
            regbutton.grid(pady=3)

            logoutb = tk.Button(
            text = "EXIT",
            foreground = "red",
            background = "cyan",
            width = 10,
            height = 1, master=logfra, command=loginadmin.destroy
            )
            logoutb.grid(pady=3)


        submitbtn = tk.Button(
        text = "LOGIN",
        foreground = "green",
        background = "cyan",
        width = 10,
        height = 1, master=logframe,
        command=loginadmin
        )
        submitbtn.grid(pady=3)

        logoutbutton = tk.Button(
        text = "EXIT",
        foreground = "red",
        background = "cyan",
        width = 10,
        height = 1, master=logframe, command=login.destroy
        )
        logoutbutton.grid(pady=3)

logbutton = tk.Button(
text = "Login/Register",
foreground = "green",
background = "cyan",
width = 25,
height = 2, master=frame1,
command=login
)
logbutton.grid(pady=3)

logoutbutton = tk.Button(
text = "EXIT",
foreground = "red",
background = "cyan",
width = 25,
height = 2, master=frame1, command=window.destroy
)
logoutbutton.grid(pady=3)

desc = tk.Label(text="We fight for every child to feel the love and belonging of a safe family home.",
foreground = "black",
background = "blue",
width = 80,
height = 2,
master=frame2,
)
desc.grid(padx=5, pady=5, column=3, row=4)

window.mainloop()