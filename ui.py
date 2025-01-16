from tkinter import *
e=-1
def ret():
    logWindow = Tk()
    logWindow.geometry('1000x600+120+50')
    logWindow.title('Functions')
    logWindow.configure(bg="#3D3D3D")
    def fun1():
        logWindow.destroy()
        global e
        e=1
    def fun2():
        logWindow.destroy()
        global e
        e=2
    def fun3():
        logWindow.destroy()
        global e
        e=3
    def fun4():
        logWindow.destroy()
        global e
        e=4
    def fun5():
        logWindow.destroy()
        global e
        e=5
    def fun6():
        logWindow.destroy()
        global e
        e=6
    def fun7():
        logWindow.destroy()
        global e
        e=7
    def fun8():
        logWindow.destroy()
        global e
        e=8
    def exi():
        logWindow.destroy()
        global e
        e=-2
    fun1Button = Button(logWindow, bg="#1ADC5B", text='Top 10 words\nin wordcloud', font=("Times New Roman", 18), command=fun1)
    fun1Button.place(relx=0.3, rely=0.2, anchor=CENTER)
    fun2Button = Button(logWindow, bg="#1ADC5B", text='messages sent \nby DOW', font=("Times New Roman", 18), command=fun2)
    fun2Button.place(relx=0.5, rely=0.2, anchor=CENTER)
    fun3Button = Button(logWindow, bg="#1ADC5B", text='messages sent \nby month', font=("Times New Roman", 18), command=fun3)
    fun3Button.place(relx=0.7, rely=0.2, anchor=CENTER)
    fun4Button = Button(logWindow, bg="#1ADC5B", text='Avg Response\nTime', font=("Times New Roman", 18), command=fun4)
    fun4Button.place(relx=0.3, rely=0.4, anchor=CENTER)
    fun5Button = Button(logWindow, bg="#1ADC5B", text='Conversation Start \nPlot', font=("Times New Roman", 18), command=fun5)
    fun5Button.place(relx=0.5, rely=0.4, anchor=CENTER)
    fun6Button = Button(logWindow, bg="#1ADC5B", text='Chat Activity \nPlot', font=("Times New Roman", 18), command=fun6)
    fun6Button.place(relx=0.4, rely=0.6, anchor=CENTER)
    fun8Button = Button(logWindow, bg="#1ADC5B", text='Distribution Of \nTexts', font=("Times New Roman", 18),command=fun8)
    fun8Button.place(relx=0.7, rely=0.4, anchor=CENTER)
    fun7Button = Button(logWindow, bg="#1ADC5B", text='Length of Message\nPlot', font=("Times New Roman", 18),command=fun7)
    fun7Button.place(relx=0.6, rely=0.6, anchor=CENTER)

    exitButton = Button(logWindow, fg="#ff0000", bg="#1ADC5B", text='exit', font=("Times New Roman", 20), command=exi)
    exitButton.place(relx=0.5, rely=0.9, anchor=CENTER)

    logWindow.attributes('-topmost', True)
    logWindow.mainloop()

    return e
