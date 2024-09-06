from tkinter import *
from tkinter import messagebox
from option import *

class WelcomePage:
    def welcomepage(self):
        with open('clientDetails.txt', 'r') as f:
            data = f.read()
        name, number = data.split(',')

        welcomeRoot = Tk()
        welcomeRoot.configure(bg="magenta2")
        welcomeRoot.resizable(False, False)
        welcomeRoot.geometry("420x300+500+150")
        welcomeRoot.title(f"ওহে! মি. {name} আপনাকে স্বাগতম")
        label = Label(welcomeRoot, text=f"\nওহে ! মি. {name}\nআপনাকে গণনাকারী যন্ত্রে\nস্বাগতম। "
                                        f"অনুগ্রহ করে নিশ্চিত করুন\n যে এটা আপনার\n"
                                        f"নাম্বার : {number}", font=("arial", 16, "bold", "italic"),bg="magenta3",fg="medium spring green",width=29,height=7)

        label.place(x=20,y=20)
        def ConfirmButton():
            welcomeRoot.destroy()
            option = Option()
            option.option()
        confirmButton = Button(welcomeRoot, text="নিশ্চিত করুন", font=("times new roman", 26, "bold"),
                               bg="magenta3", activebackground="magenta2",fg="spring green",activeforeground="spring green", command=ConfirmButton)
        confirmButton.place(x=80, y=210)

        welcomeRoot.mainloop()
