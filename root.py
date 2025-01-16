from tkinter import *

e = ''


def filepth():
    logWindow = Tk()
    logWindow.geometry('1000x600+120+50')
    logWindow.title('CAPTCHA')
    logWindow.configure(bg="#3D3D3D")

    def confirm():
        global e
        e = usernameEntry.get()
        if e.startswith('"') or e.startswith("'"):
            e = e[1:-1:1]

        logWindow.destroy()

    usernameLabel1 = Label(logWindow, bg="#3D3D3D", fg="#FFFFFF", text="Enter file location",
                           font=("Times New Roman", 30))
    usernameLabel1.place(relx=0.27, rely=0.5, anchor=CENTER)
    username = StringVar()
    usernameEntry = Entry(logWindow, textvariable=username, font=("Times New Roman", 20), width=15)
    usernameEntry.place(relx=0.55, rely=0.5, anchor=CENTER)
    enterButton = Button(logWindow, bg="#1ADC5B", text='ENTER', font=("Times New Roman", 20), command=confirm)
    enterButton.place(relx=0.76, rely=0.5, anchor=CENTER)

    logWindow.attributes('-topmost', True)
    logWindow.mainloop()
    return (e)