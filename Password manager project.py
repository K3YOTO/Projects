import tkinter as Tk
from tkinter import messagebox

def add():
    #accepting input from user
    username = entryName.get()
    #accepting password input from user
    password = entryPassword.get()
    if username and password:
        with open("passwords.txxt", 'a') as f:
            f.write(f"{username} {password}\n")
            messagebox.showinfo("sucess", "password added")
    else:
        messagebox.showinfo("error", "please enter both fields")

def get():
    #accept input from user
    username = entryName.get()

    #create dictionary to store data in form of key value pairs
    passwords = {}
    try:
        #opening the text file
        with open ("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                #creating the key-value for pair of username and password
                passwords[i[0]] = i[1]
    
    except:
        #displaying error
        print("error")
    
    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No such username exists"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "empty list")

def delete():
    #accepting input from user
    username = entryName.get()
    # creating a temporary list to store data
    temp_passwords = []

    #reading data from the file and excluding the specified username
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")

        #writing modified data back to the file
        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line)

        messagebox.showinfo(
            "success", f"User {username} deleted successfully")
    except Exception as e:
        messagebox.showerror("error", f"error deleting user {username}: {e}") 

def getList():
    #creating dictionary
    passwords = {}
    #adding a try block to catch errors such as empty file or others
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("no passwords found")

    if passwords:
        mess = "list of passwords\n"
        for name, passowrd, in passwords.items():
        #generating proper message
            mess += f"password for {name} is {password}\n" 
            messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "empty list")      

if __name__ == "__main__":
    app = Tk.Tk()
    app.geometry("560x270")
    app.title("Manny's Prototype project")

    #username block
    labelName = Tk.Label(app, text="USERNAME")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = Tk.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    #password block
    labelPassword = Tk.Label(app, text="PASSWORD")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = Tk.Entry(app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    #add button
    buttonAdd = Tk.Button(app, text="add", command=add)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    #get button
    buttonGet = Tk.Button(app, text="get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    #list button
    buttonList = Tk.Button(app, text="List", command=get)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")
    
    # Delete button
    buttonDelete = Tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()
