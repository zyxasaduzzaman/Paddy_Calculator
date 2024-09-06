from tkinter import *
from tkinter import messagebox
from welcomePage import *



homeRoot = Tk()
font = ("arial", 14, "bold")
homeRoot.title("আপনাকে নতুন গণনাকারী যন্ত্রে স্বাগতম")
homeRoot.configure(bg="magenta3")
homeRoot.geometry("480x270+500+150")
homeRoot.resizable(False, False)
welLabel = Label(homeRoot, font=("arial", 16, "bold", "italic"), text="ওহে ! মি. আপনাকে গণনাকারী যন্ত্রে স্বাগতম\n"
                                                                      "চালিয়ে যেতে কিছু বসান...", bg="magenta3",fg="medium spring green")
welLabel.place(x=20,y=20)

nameLabel = Label(homeRoot, font=font, text="ক্লায়েন্টের নাম বসান : ", bg="magenta3",fg="medium spring green")
nameLabel.place(x=20, y=100)
numberLabel = Label(homeRoot, font=font, text="ক্লায়েন্টের নাম্বার বসান : ",bg="magenta3",fg="medium spring green")
numberLabel.place(x=20, y=140)

nameVar = StringVar()
numberVar = StringVar()
nameEntry = Entry(homeRoot, font=font, textvariable=nameVar)
nameEntry.place(x=240, y=100)
numberEntry = Entry(homeRoot, font=font, textvariable=numberVar)
numberEntry.place(x=240, y=140)


def GoButton():
    if nameVar.get() == "" or numberVar.get() == "":
        messagebox.showwarning("সতর্কবাণী", "নাম ও নাম্বারের জায়গাটি ফাঁকা আছে")
    else:
        with open("clientDetails.txt", "w") as f:
            f.write(f"{nameVar.get()},{numberVar.get()}")
        homeRoot.destroy()
        wp = WelcomePage()
        wp.welcomepage()

def ClearButton():
    if nameVar.get() == "" and numberVar.get() == "":
        messagebox.showwarning("সতর্কবাণী", "জায়গাটি ফাঁকা আছে")
    else:
        numberVar.set("")
        nameVar.set("")

clearButton = Button(homeRoot, text="মুছুন", font=("times new roman", 26, "bold"), width=6, bg="magenta2",
                     activebackground="magenta4", command=ClearButton,fg="SpringGreen")
clearButton.place(x=50, y=185)
goButton = Button(homeRoot, text="যান", font=("times new roman ", 26, "bold"), width=6, bg="magenta2",
                  activebackground="magenta4", command=GoButton,fg="SpringGreen")
goButton.place(x=300, y=185)
homeRoot.mainloop()
