from tkinter import *
from datetime import datetime
from PIL import ImageGrab
import os

class Final:
    def final(self):
        font = ("arial", 20, "bold")
        self.finalRoot = Tk()
        self.current_date = datetime.now()
        self.formatted_date = self.current_date.strftime("%d/%m/%Y")
        self.formatted_time = self.current_date.strftime("%I:%M:%S %p")
        self.day_name = self.current_date.strftime("%A")
        self.finalRoot.title("এটি মূল তথ্য.....")
        self.finalRoot.resizable(False, False)
        self.finalRoot.geometry("700x700+200+0")
        self.finalRoot.configure(bg="purple4")

        self.dateLabel = Label(self.finalRoot, text=f"তারিখ: {self.formatted_date}", fg="white", font=("arial", 16, "bold", "italic"), bg="purple4")
        self.dateLabel.place(x=5, y=5)
        self.day_nameLabel = Label(self.finalRoot, text=f"বার : {self.day_name}", fg="white", font=("arial", 16, "bold", "italic"), bg="purple4")
        self.day_nameLabel.place(x=540, y=5)

        try:
            with open('clientDetails.txt', 'r') as f:
                data = f.read().strip()
            name, Mnumber = data.split(',')
        except FileNotFoundError:
            print("clientDetails.txt not found.")
            return
        except ValueError:
            print("Error reading clientDetails.txt. Ensure it contains 'name,Mnumber'.")
            return

        try:
            with open("all.txt", "r") as f1:
                data1 = f1.read().strip()
            totalSack, totalWeight, toOmit, rate = data1.split(",")
        except FileNotFoundError:
            print("all.txt not found.")
            return
        except ValueError:
            print("Error reading all.txt. Ensure it contains 'totalSack,totalWeight,toOmit,rate'.")
            return

        self.clietName = Label(self.finalRoot, text=f"ক্লায়েন্টের নাম\t\t:   {name}", font=font, bg="purple4", fg="white")
        self.clietName.place(x=20, y=70)
        self.clietNumber = Label(self.finalRoot, text=f"ক্লায়েন্টের নাম্বার \t\t:   {Mnumber}", font=font, bg="purple4", fg="white")
        self.clietNumber.place(x=20, y=110)
        self.totalSackLabel = Label(self.finalRoot, text=f"মোট বস্তু \t\t\t:   {totalSack}", font=font, bg="purple4", fg="white")
        self.totalSackLabel.place(x=20, y=150)
        self.totalWeightLabel = Label(self.finalRoot, text=f"মোট ওজন \t\t:   {totalWeight}", font=font, bg="purple4", fg="white")
        self.totalWeightLabel.place(x=20, y=190)
        self.toOmitLabel = Label(self.finalRoot, text=f"বস্তু প্রতি ছাড়তে হবে \t:   {toOmit}", font=font, bg="purple4", fg="white")
        self.toOmitLabel.place(x=20, y=230)
        self.rateLabel = Label(self.finalRoot, text=f"বস্তু প্রতি দাম \t\t:   {rate}", font=font, bg="purple4", fg="white")
        self.rateLabel.place(x=20, y=270)

        netWeight = float(totalWeight) - (float(totalSack) * float(toOmit))

        self.netWeightLabel = Label(self.finalRoot, text=f"বস্তু প্রতি ছেড়ে ওজন \t:   {netWeight}", font=font, bg="purple4", fg="white")
        self.netWeightLabel.place(x=20, y=310)
        singlePrice = float(rate) / 80
        netPrice = (float(netWeight) * singlePrice)
        self.netPriceLabel = Label(self.finalRoot, text=f"মোট দাম \t\t:   {netPrice:.2f}", font=font, bg="purple4", fg="white")
        self.netPriceLabel.place(x=20, y=350)
        self.singelPriceLabel = Label(self.finalRoot, text=f"প্রতি কেজির দাম \t\t:   {singlePrice:.2f}", font=font, bg="purple4", fg="white")
        self.singelPriceLabel.place(x=20, y=390)

        self.totalMaund = float(totalWeight) / 40
        self.netMaund = float(netWeight) / 40
        self.totalMaundLabel = Label(self.finalRoot, font=font, bg="purple4", text=f"মোট মণ \t\t\t:   {self.totalMaund:.2f}", fg="white")
        self.totalMaundLabel.place(x=20, y=430)
        self.netMaundLabel = Label(self.finalRoot, font=font, bg="purple4", text=f"ওজন ছেড়ে মণ \t\t:   {self.netMaund:.2f}", fg="white")
        self.netMaundLabel.place(x=20, y=470)

        self.dellerLabel = Label(self.finalRoot, text="ডিলার", font=font, bg="purple4", fg="white")
        self.dellerLabel.place(x=20, y=570)
        self.clientLabel = Label(self.finalRoot, text="ক্লায়েন্ট", font=font, bg="purple4", fg="white")
        self.clientLabel.place(x=530, y=570)

        self.print = Button(self.finalRoot, text="PRINT", font=("times new roman", 26, "bold"), bg="white", fg="red", activeforeground="red", activebackground="pink", command=lambda: self.take_screenshot(name, Mnumber))
        self.print.place(x=530, y=620)

        self.t1 = Label(self.finalRoot, text=f"Time : {self.formatted_time}", font=("arial", 16, "bold"), bg="purple4", fg="white")
        self.t1.place(x=20, y=650)

        self.finalRoot.mainloop()

    def take_screenshot(self, name, Mnumber):
        x = self.finalRoot.winfo_rootx()
        y = self.finalRoot.winfo_rooty()
        w = x + self.finalRoot.winfo_width()
        h = y + self.finalRoot.winfo_height()
        screenshot = ImageGrab.grab().crop((x, y, w, h))
        save_dir = r"C:\Users\hp\Pictures\screenshot"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_path = os.path.join(save_dir, f"{name.strip()}{Mnumber.strip()}.png")
        screenshot.save(save_path)
        self.finalRoot.destroy()
        print(f"Screenshot taken and saved as '{save_path}'")

