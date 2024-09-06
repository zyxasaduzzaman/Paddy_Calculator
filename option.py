from tkinter import *
from sack import *
from noSack import *


class Option:
    def option(self):
        def on_checkbox_click():
            if yesVar.get()=="yes":
                optionRoot.destroy()
                noSack = NoSack()
                noSack.noSack()

            else:
                optionRoot.destroy()
                sack = Sack()
                sack.sack()

        optionRoot = Tk()
        optionRoot.resizable(False,False)
        optionRoot.configure(bg="spring green")
        optionRoot.geometry("400x130+500+200")
        optionRoot.title("অপশন নির্বাচন করুন...")

        yesVar = StringVar(value="no")
        noVar = StringVar(value="no")

        yesCheckBox = Checkbutton(optionRoot, onvalue="yes", offvalue="no", variable=yesVar,
                                  text="মোট করা আছে", font=("arial", 20, "bold"),
                                  bg="spring green", activebackground="spring green", fg="brown",activeforeground="brown",
                                  command=on_checkbox_click)
        yesCheckBox.place(x=50, y=20)

        noCheckBox = Checkbutton(optionRoot, onvalue="yes", offvalue="no", variable=noVar,
                                 text="মোট করা নাই", font=("arial", 20, "bold"),
                                 bg="spring green", activebackground="spring green", fg="brown",activeforeground="brown",
                                 command=on_checkbox_click)
        noCheckBox.place(x=50, y=60)

        optionRoot.mainloop()

