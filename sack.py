from tkinter import *
from tkinter import messagebox
from final import *

class Sack:
    def sack(self):
        self.sackRoot = Tk()
        self.sackRoot.title("গণনা চলছে....")
        self.sackRoot.resizable(False, False)
        self.sackRoot.geometry("1250x680+50+0")
        self.sackRoot.configure(bg="navy")

        self.label_counter = 1  # Initialize the counter here
        self.total_sacks = 0
        self.total_weight = 0.0
        self.sacks = {}

        self.mainFrame()
        self.sackRoot.mainloop()

    def create_scrollbar(self, parent):
        scrollbar = Scrollbar(parent)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas = Canvas(parent, bg="blue2", yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        frame = Frame(canvas, bg="blue2")
        canvas.create_window((0, 0), window=frame, anchor='nw')

        frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Bind mouse wheel event to canvas for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        return frame

    def mainFrame(self):
        self.mFrame = Frame(self.sackRoot, bg="brown4")
        self.mFrame.place(x=10, y=10, width=830, height=660)
        self.mmL = Label(self.mFrame, text="গণনার বর্ণনা", font=("arial", 26, "bold"), bg="brown4", fg="darkblue")
        self.mmL.place(x=250, y=0)
        self.sideFrame()
        self.downFrame()

        self.lMFrame = Frame(self.mFrame, bg="brown4")
        self.lMFrame.place(x=0, y=50, width=350, height=610)
        self.totalSackLabel = Label(self.lMFrame, text=f"মোট গণনা: {self.total_sacks}", font=("arial", 20, "bold"), bg="brown4")
        self.totalSackLabel.place(x=10, y=5)
        self.totalWeightLabel = Label(self.lMFrame, text=f"মোট ওজন: {self.total_weight}", font=("arial", 20, "bold"), bg="brown4")
        self.totalWeightLabel.place(x=10, y=50)

        self.omitLabel = Label(self.lMFrame, text="ছাড়তে হবে:", font=("arial", 20, "bold"), bg="brown4")
        self.omitLabel.place(x=10, y=150)
        self.omitVar = StringVar()
        self.omitEntry = Entry(self.lMFrame, font=("arial", 20, "bold"), bg="white",textvariable=self.omitVar)
        self.omitEntry.place(x=180, y=150)

        self.rateLabel = Label(self.lMFrame, text="বাজার মূল্য:", font=("arial", 20, "bold"), bg="brown4")
        self.rateLabel.place(x=10, y=200)
        self.rateVar = StringVar()
        self.rateEntry = Entry(self.lMFrame, font=("arial", 20, "bold"), bg="white",textvariable=self.rateVar)
        self.rateEntry.place(x=180, y=200)

        self.rMFrame = Frame(self.mFrame, bg="red")
        self.rMFrame.place(x=380, y=50, width=450, height=450)
        self.rMFrame_inner = self.create_scrollbar(self.rMFrame)

        self.scrClear = Button(self.mFrame, text="মুছুন", font=("arial", 20, "bold"), bg="white", activebackground="brown4", command=self.SCRClear)
        self.scrClear.place(x=400, y=550)

        self.delete = Button(self.mFrame, text="ছাটাই", font=("arial", 20, "bold"), bg="white", activebackground="brown4", command=self.delete_last_sack)
        self.delete.place(x=600, y=550)

        def Submit():
            if self.rateVar.get()!="" and self.omitVar.get()!="":
                try:
                    self.totalSacks = int(self.total_sacks)
                    self.totalWeight = float(self.total_weight)
                    self.toOmit = float(self.omitVar.get())
                    self.Rate = float(self.rateVar.get())
                    with open("all.txt","w") as f:
                        f.write(f"{self.totalSacks},{self.totalWeight},{self.toOmit},{self.Rate}")
                        f.close()
                    self.sackRoot.destroy()
                    f = Final()
                    f.final()
                except ValueError:
                    messagebox.showwarning("সতর্কবাণী","ভুল ইনপুট")
                    self.omitVar.set("")
                    self.rateVar.set("")
            else:
                messagebox.showwarning("সতর্কবাণী","রেট ও অমিটের জায়গা খালি আছে")
        def MClear():
            if self.rateVar.get() != "" and self.omitVar.get() != "":
                self.omitVar.set("")
                self.rateVar.set("")
            else:
                messagebox.showwarning("সতর্কবাণী","রেট ও অমিটের জায়গা খালি আছে")

        self.submit = Button(self.mFrame, text="সাবমিট", font=("arial", 26, "bold"), bg="white",
                             activebackground="pink", width=15, state="disabled",command=Submit)
        self.submit.place(x=20, y=460)

        self.next = Button(self.mFrame, text="তারপর", font=("arial", 26, "bold"), bg="white", activebackground="pink",
                           width=15, command=self.enable_submit)
        self.next.place(x=20, y=300)

        self.mClear = Button(self.mFrame, text="মুছুন", font=("arial", 26, "bold"), bg="white", activebackground="pink",
                             width=15,command=MClear)
        self.mClear.place(x=20, y=380)

    def enable_submit(self):
        self.submit.config(state="normal")

    def sideFrame(self):
        self.sFrame = Frame(self.sackRoot, bg="purple1")
        self.sFrame.place(x=850, y=10, width=390, height=270)
        self.mainLabel = Label(self.sFrame, text="এটি ইনপুটের জায়গা", font=("arial", 26, "bold"), fg="black", bg="purple1")
        self.mainLabel.place(x=30, y=30)

        self.wLabel = Label(self.sFrame, text="বস্তুর ওজন বসান", font=("arial", 20, "bold"), fg="white", bg="purple1")
        self.wLabel.place(x=80, y=90)

        self.weightVar = StringVar()
        self.wEntry = Entry(self.sFrame, font=("arial", 20, "bold"), fg="black", bg="white", textvariable=self.weightVar)
        self.wEntry.place(x=50, y=130)

        def SClear():
            if self.weightVar.get() == "":
                messagebox.showwarning("সতর্কবাণী", "জায়গাটি খালি আছে")
            else:
                self.weightVar.set("")

        self.sClear = Button(self.sFrame, text="মুছুন", font=("times new roman", 26, "bold"), command=SClear, bg="white", activebackground="lightblue")
        self.sClear.place(x=5, y=180)

        def SAdd():
            weight = self.weightVar.get()
            if weight:
                try:
                    weight = float(weight)
                    # Create a new label in the rMFrame with the entered weight
                    new_label = Label(self.rMFrame_inner, text=f"{self.label_counter} নাম্বার বস্তুর ওজন হচ্ছে : {weight}", font=("arial", 16), bg="blue2",fg="white")
                    self.sacks[self.label_counter] = weight  # Store the weight in the sacks dictionary
                    self.label_counter += 1
                    new_label.pack(anchor='w', padx=10, pady=5)
                    self.weightVar.set("")
                    # Update total sacks and total weight
                    self.total_sacks += 1
                    self.total_weight += weight
                    self.update_totals()
                except ValueError:
                    messagebox.showwarning("সতর্কবাণী", "ভুল ইনপুট")
                    self.weightVar.set("")
            else:
                messagebox.showwarning("সতর্কবাণী", "জায়গাটি খালি আছে")

        self.sAdd = Button(self.sFrame, text="চালান", command=SAdd, font=("times new roman", 26, "bold"), bg="white", activebackground="lightblue")
        self.sAdd.place(x=250, y=180)

    def downFrame(self):
        self.dFrame = Frame(self.sackRoot, bg="darkgreen")
        self.dFrame.place(x=850, y=290, width=390, height=380)

        self.dLabel = Label(self.dFrame, text="এটি সংশোধনের জায়গা", font=("arial", 20, "bold"), fg="black", bg="darkgreen")
        self.dLabel.place(x=30, y=20)

        self.numOfSackLabel = Label(self.dFrame, text="বস্তুর নাম্বার বসান:", font=("arial", 16, "bold"), bg="darkgreen", fg="white")
        self.numOfSackLabel.place(x=10, y=100)

        self.sackNumberVar = StringVar()
        self.numOfSackEntry = Entry(self.dFrame, font=("arial", 20, "bold"), bg="white", width=7, textvariable=self.sackNumberVar)
        self.numOfSackEntry.place(x=250, y=100)

        self.newSackWeightLabel = Label(self.dFrame, text="বস্তুর নতুন ওজন বসান:", font=("arial", 16, "bold"), fg="white", bg="darkgreen")
        self.newSackWeightLabel.place(x=10, y=160)

        self.newWeightVar = StringVar()
        self.newSackWeightEntry = Entry(self.dFrame, font=("arial", 20, "bold"), bg="white", width=7, textvariable=self.newWeightVar)
        self.newSackWeightEntry.place(x=250, y=160)

        def DClear():
            if self.sackNumberVar.get() == "" and self.newWeightVar.get() == "":
                messagebox.showwarning("সতর্কবাণী", "জায়গাটি খালি আছে")
            else:
                self.sackNumberVar.set("")
                self.newWeightVar.set("")

        def DAdd():
            sack_number = self.sackNumberVar.get()
            new_weight = self.newWeightVar.get()
            if sack_number and new_weight:
                try:
                    sack_number = int(sack_number)
                    new_weight = float(new_weight)
                    if sack_number in self.sacks:
                        old_weight = self.sacks[sack_number]
                        self.total_weight -= old_weight  # Subtract the old weight
                        self.total_weight += new_weight  # Add the new weight
                        self.sacks[sack_number] = new_weight
                        self.update_totals()
                        # Update the label in rMFrame_inner
                        for widget in self.rMFrame_inner.winfo_children():
                            if widget.cget("text").startswith(f"{sack_number} নাম্বার বস্তুর ওজন হচ্ছে :"):
                                widget.config(text=f"{sack_number} নাম্বার বস্তুর ওজন হচ্ছে : {new_weight}")
                        self.sackNumberVar.set("")
                        self.newWeightVar.set("")
                    else:
                        messagebox.showwarning("সতর্কবাণী", "এরকম কোনো বস্তুর নাম্বার নেই")
                except ValueError:
                    messagebox.showwarning("সতর্কবাণী", "ভুল ইনপুট")
            else:
                messagebox.showwarning("সতর্কবাণী", "জায়গাটি খালি আছে")

        self.dClear = Button(self.dFrame, text="মুছুন", command=DClear, font=("times new roman", 26, "bold"), bg="white", activebackground="lightgreen")
        self.dClear.place(x=5, y=290)
        self.dAdd = Button(self.dFrame, text="চালান", command=DAdd, font=("times new roman", 26, "bold"), bg="white", activebackground="lightgreen")
        self.dAdd.place(x=250, y=290)

    def SCRClear(self):
        if not self.rMFrame_inner.winfo_children():
            messagebox.showwarning("সতর্কবাণী", "জায়গাটি খালি আছে")
        else:
            for widget in self.rMFrame_inner.winfo_children():
                widget.destroy()
            self.total_sacks = 0
            self.total_weight = 0.0
            self.sacks.clear()
            self.label_counter = 1
            self.update_totals()

    def delete_last_sack(self):
        if not self.sacks:
            messagebox.showwarning("সতর্কবাণী", "মুছার জন্য বস্তু নেই")
        else:
            last_label = self.rMFrame_inner.winfo_children()[-1]
            last_label.destroy()
            last_sack_number = self.label_counter - 1
            if last_sack_number in self.sacks:
                last_weight = self.sacks.pop(last_sack_number)
                self.total_weight -= last_weight
                self.total_sacks -= 1
                self.label_counter -= 1
                self.update_totals()

    def update_totals(self):
        self.totalSackLabel.config(text=f"মোট বস্তু : {self.total_sacks}")
        self.totalWeightLabel.config(text=f"মোট ওজন : {self.total_weight}")

