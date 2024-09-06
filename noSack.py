from tkinter import *
from tkinter import messagebox
from final import *

class NoSack:
    def noSack(self):
        noSackRoot = Tk()
        font = ("arial",20,"bold")
        noSackRoot.geometry("750x350+450+200")
        noSackRoot.title("মোট হিসান বসান")
        noSackRoot.configure(bg="brown4")
        noSackRoot.resizable(False,False)
        tWeightLabel = Label(noSackRoot,text="মোট ওজন : ",font=font,bg="brown4",fg="cyan")
        tWeightLabel.place(x=110,y=50)
        tSacksLabel = Label(noSackRoot,text="মোট বস্তু সংখ্যা : ",font=font,bg="brown4",fg="cyan")
        tSacksLabel.place(x=110,y=100)
        toOmitLabel = Label(noSackRoot,text="বস্তু প্রতি ছাড়তে হবে : ",font=font,bg="brown4",fg="cyan")
        toOmitLabel.place(x=110,y=150)
        rateLabel = Label(noSackRoot,text="বাজার মূল্য : ",font=font,bg="brown4",fg="cyan")
        rateLabel.place(x=110,y=200)



        weightVar = StringVar()
        sackVar = StringVar()
        toOMitVar = StringVar()
        rateVar= StringVar()


        tWeightEntry = Entry(noSackRoot,font=font,width=15,textvariable=weightVar)
        tWeightEntry.place(x=420,y=50)
        tSacksEntry = Entry(noSackRoot,font=font,width=15,textvariable=sackVar)
        tSacksEntry.place(x=420,y=100)
        toOmitEntry = Entry(noSackRoot,font=font,width=15,textvariable=toOMitVar)
        toOmitEntry.place(x=420,y=150)
        rateEntry = Entry(noSackRoot,font=font,width=15,textvariable=rateVar)
        rateEntry.place(x=420,y=200)


        def Clear():
            if weightVar.get()=="" and sackVar.get()=="" and toOMitVar.get()=="" and rateVar.get()=="":
                messagebox.showwarning("সতর্কবাণী","জায়গা ইতিমধ্যে খালি আছে")
            else:
                weightVar.set("")
                sackVar.set("")
                toOMitVar.set("")
                rateVar.set("")
        def Submit():
            if weightVar.get()!="" and sackVar.get()!="" and toOMitVar.get()!="" and rateVar.get()!="":
                try:
                    totalWight = float(weightVar.get())
                    totalSacks = int(sackVar.get())
                    toOmit = float(toOMitVar.get())
                    rate = float(rateVar.get())
                    with open("all.txt", "w") as f:
                        f.write(f"{totalSacks},{totalWight},{toOmit},{rate}")
                        f.close()
                    noSackRoot.destroy()
                    f = Final()
                    f.final()
                except ValueError:
                    messagebox.showwarning("সতর্কবাণী", "ভুল ইনপুট")
                    weightVar.set("")
                    sackVar.set("")
                    toOMitVar.set("")
                    rateVar.set("")

            else:
                messagebox.showwarning("সতর্কবাণী", "জায়গা খালি আছে")
        clearButton = Button(noSackRoot,font=font,text="মুছুন",bg="white",activebackground="lightblue",width=8,command=Clear)
        clearButton.place(x=200,y=270)
        submitButton = Button(noSackRoot,font=font,text="সাবমিট",bg="white",activebackground="lightblue",width=8,command=Submit)
        submitButton.place(x=450,y=270)
        noSackRoot.mainloop()