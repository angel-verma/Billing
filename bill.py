from tkinter import*
import math
import random
from tkinter import messagebox
import os


class Bill:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")

        bg = "#074463"
        title = Label(self.root, text="Billing Software",
                      font="arial 30 bold", bd=10, relief=GROOVE, bg=bg, pady=10, fg="white")
        title.pack(fill=X)

        # ========variables==============
        # cosmetics
        self.soap = IntVar()
        self.fc = IntVar()
        self.fw = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()
        # grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # Cold Drink
        self.maaza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        # total product price and tax variable
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # customer
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.billno = StringVar()
        x = random.randint(1000, 9999)
        self.billno.set(str(x))

        self.search_bill = StringVar()

        # ===================customer details frame====================
        f1 = LabelFrame(self.root, text="Customer Details",
                        font="arial 15 bold", fg="gold", bg=bg, bd=10, relief=GROOVE)
        f1.place(x=0, y=80, relwidth=1)

        lcustomer = Label(f1, text="Customer Name",
                          font="arial 15 bold", bg=bg, fg="white")
        lcustomer.grid(row=0, column=0, padx=20, pady=10)
        tcustomer = Entry(f1, width=15, font="arial 15 bold", textvariable=self.c_name,
                          bd=5, relief=SUNKEN)
        tcustomer.grid(row=0, column=1, pady=5)

        lphone = Label(f1, text="Phone Number",
                       font="arial 15 bold", bg=bg, fg="white")
        lphone.grid(row=0, column=2, padx=20, pady=10)
        tphone = Entry(f1, width=15, font="arial 15 bold", bd=5,
                       relief=SUNKEN, textvariable=self.c_phone)
        tphone.grid(row=0, column=3, pady=5)

        lbill = Label(f1, text="Bill Number",
                      font="arial 15 bold", bg=bg, fg="white")
        lbill.grid(row=0, column=4, padx=20, pady=10)
        tbill = Entry(f1, width=15, font="arial 15 bold", bd=5,
                      relief=SUNKEN, textvariable=self.search_bill)
        tbill.grid(row=0, column=5, pady=5)

        bbill = Button(f1, text="Search", width=10, bd=5, command=self.find_bill,
                       relief=GROOVE, font="arial 14 bold")
        bbill.grid(row=0, column=6, pady=10, padx=20)

        # =======================Cosmetic Frame=========================
        f2 = LabelFrame(self.root, text="Cosmetics",
                        font="arial 15 bold", fg="gold", bg=bg, bd=10, relief=GROOVE)
        f2.place(x=5, y=180, width=325, height=380)

        lbath = Label(f2, text="Bath Soap", font="arial 16 bold",
                      bg=bg, fg="light green")
        lbath.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        tbath = Entry(f2, width=15, bd=5, relief=SUNKEN,
                      textvariable=self.soap)
        tbath.grid(row=0, column=1, padx=10, pady=10)

        lface = Label(f2, text="Face Cream",
                      font="arial 16 bold", bg=bg, fg="light green")
        lface.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        tface = Entry(f2, width=15, bd=5, relief=SUNKEN, textvariable=self.fc)
        tface.grid(row=1, column=1, padx=10, pady=10)

        lfacewash = Label(f2, text="Face Wash",
                          font="arial 16 bold", bg=bg, fg="light green")
        lfacewash.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        tfacewash = Entry(f2, width=15, bd=5, relief=SUNKEN,
                          textvariable=self.fw)
        tfacewash.grid(row=2, column=1, padx=10, pady=10)

        lhairspray = Label(f2, text="Hair Spray",
                           font="arial 16 bold", bg=bg, fg="light green")
        lhairspray.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        thairspray = Entry(f2, width=15, bd=5, relief=SUNKEN,
                           textvariable=self.spray)
        thairspray.grid(row=3, column=1, padx=10, pady=10)

        lhairgel = Label(f2, text="Hair Gel",
                         font="arial 16 bold", bg=bg, fg="light green")
        lhairgel.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        thairgel = Entry(f2, width=15, bd=5, relief=SUNKEN,
                         textvariable=self.gell)
        thairgel.grid(row=4, column=1, padx=10, pady=10)

        lbodylotion = Label(f2, text="Body Lotion",
                            font="arial 16 bold", bg=bg, fg="light green")
        lbodylotion.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        tbodylotion = Entry(f2, width=15, bd=5,
                            relief=SUNKEN, textvariable=self.lotion)
        tbodylotion.grid(row=5, column=1, padx=10, pady=10)

        # =======================Grocery Product Frame=========================
        f3 = LabelFrame(self.root, text="Grocery Product",
                        font="arial 15 bold", fg="gold", bg=bg, bd=10, relief=GROOVE)
        f3.place(x=340, y=180, width=325, height=380)

        lrice = Label(f3, text="Rice", font="arial 16 bold",
                      bg=bg, fg="light green")
        lrice.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        trice = Entry(f3, width=15, bd=5, relief=SUNKEN,
                      textvariable=self.rice)
        trice.grid(row=0, column=1, padx=10, pady=10)

        lfoodoil = Label(f3, text="Food Oil",
                         font="arial 16 bold", bg=bg, fg="light green")
        lfoodoil.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        tfoodoil = Entry(f3, width=15, bd=5, relief=SUNKEN,
                         textvariable=self.food_oil)
        tfoodoil.grid(row=1, column=1, padx=10, pady=10)

        ldaal = Label(f3, text="Daal", font="arial 16 bold",
                      bg=bg, fg="light green")
        ldaal.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        tdaal = Entry(f3, width=15, bd=5, relief=SUNKEN,
                      textvariable=self.daal)
        tdaal.grid(row=2, column=1, padx=10, pady=10)

        lwheat = Label(f3, text="Wheat", font="arial 16 bold",
                       bg=bg, fg="light green")
        lwheat.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        twheat = Entry(f3, width=15, bd=5, relief=SUNKEN,
                       textvariable=self.wheat)
        twheat.grid(row=3, column=1, padx=10, pady=10)

        lsugar = Label(f3, text="Sugar", font="arial 16 bold",
                       bg=bg, fg="light green")
        lsugar.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        tsugar = Entry(f3, width=15, bd=5, relief=SUNKEN,
                       textvariable=self.sugar)
        tsugar.grid(row=4, column=1, padx=10, pady=10)

        ltea = Label(f3, text="Tea", font="arial 16 bold",
                     bg=bg, fg="light green")
        ltea.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        ttea = Entry(f3, width=15, bd=5, relief=SUNKEN, textvariable=self.tea)
        ttea.grid(row=5, column=1, padx=10, pady=10)

        # =======================Cold Drink Frame=========================
        f4 = LabelFrame(self.root, text="Cold drink",
                        font="arial 15 bold", fg="gold", bg=bg, bd=10, relief=GROOVE)
        f4.place(x=670, y=180, width=325, height=380)

        lmaaza = Label(f4, text="Maaza", font="arial 16 bold",
                       bg=bg, fg="light green")
        lmaaza.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        tmaaza = Entry(f4, width=15, bd=5, relief=SUNKEN,
                       textvariable=self.maaza)
        tmaaza.grid(row=0, column=1, padx=10, pady=10)

        lcock = Label(f4, text="Cock", font="arial 16 bold",
                      bg=bg, fg="light green")
        lcock.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        tcock = Entry(f4, width=15, bd=5, relief=SUNKEN,
                      textvariable=self.cock)
        tcock.grid(row=1, column=1, padx=10, pady=10)

        lfrooti = Label(f4, text="Frooti", font="arial 16 bold",
                        bg=bg, fg="light green")
        lfrooti.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        tfrooti = Entry(f4, width=15, bd=5, relief=SUNKEN,
                        textvariable=self.frooti)
        tfrooti.grid(row=2, column=1, padx=10, pady=10)

        lthumbsup = Label(f4, text="Thumbs Up",
                          font="arial 16 bold", bg=bg, fg="light green")
        lthumbsup.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        tthumbsup = Entry(f4, width=15, bd=5, relief=SUNKEN,
                          textvariable=self.thumbsup)
        tthumbsup.grid(row=3, column=1, padx=10, pady=10)

        llimca = Label(f4, text="Limca", font="arial 16 bold",
                       bg=bg, fg="light green")
        llimca.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        tlimca = Entry(f4, width=15, bd=5, relief=SUNKEN,
                       textvariable=self.limca)
        tlimca.grid(row=4, column=1, padx=10, pady=10)

        lsprite = Label(f4, text="Sprite", font="arial 16 bold",
                        bg=bg, fg="light green")
        lsprite.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        tsprite = Entry(f4, width=15, bd=5, relief=SUNKEN,
                        textvariable=self.sprite)
        tsprite.grid(row=5, column=1, padx=10, pady=10)

        # =================Bill Area========================
        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1000, y=180, width=340, height=380)

        billtitle = Label(
            f5, text="Bill", font="arial 15 bold", bd=10, relief=GROOVE)
        billtitle.pack(fill=X)

        scrolly = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # ================button frame========================
        f6 = LabelFrame(self.root, text="Bill Menu",
                        font="arial 15 bold", fg="gold", bg=bg, bd=10, relief=GROOVE)
        f6.place(x=0, y=560, height=140, relwidth=1)

        lm1 = Label(f6, text="Total Cosmetic Price",
                    font="arial 14 bold", bg=bg, fg="white")
        lm1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        tm1 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.cosmetic_price)
        tm1.grid(row=0, column=1, padx=10, pady=1)

        lm2 = Label(f6, text="Total Grocery Price",
                    font="arial 14 bold", bg=bg, fg="white")
        lm2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        tm2 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.grocery_price)
        tm2.grid(row=1, column=1, padx=10, pady=1)

        lm3 = Label(f6, text="Total Cold Drink Price",
                    font="arial 14 bold", bg=bg, fg="white")
        lm3.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        tm3 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.cold_drink_price)
        tm3.grid(row=2, column=1, padx=10, pady=1)

        lm1 = Label(f6, text="Cosmetic Tax",
                    font="arial 14 bold", bg=bg, fg="white")
        lm1.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        tm1 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.cosmetic_tax)
        tm1.grid(row=0, column=3, padx=10, pady=1)

        lm2 = Label(f6, text="Grocery Tax",
                    font="arial 14 bold", bg=bg, fg="white")
        lm2.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        tm2 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.grocery_tax)
        tm2.grid(row=1, column=3, padx=10, pady=1)

        lm3 = Label(f6, text="Cold Drink Tax",
                    font="arial 14 bold", bg=bg, fg="white")
        lm3.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        tm3 = Entry(f6, width=18, bd=5, relief=SUNKEN,
                    textvariable=self.cold_drink_tax)
        tm3.grid(row=2, column=3, padx=10, pady=1)

        # =====button frame=======
        btnframe = Frame(f6, bd=5, relief=GROOVE)
        btnframe.place(x=680, width=640, height=100)

        btotal = Button(btnframe, text="Total", command=self.total, bg="cadetblue",
                        fg="white", pady=15, width=10, font="arial 14 bold", bd=5)
        btotal.grid(row=0, column=0, padx=10, pady=10)

        bgbill = Button(btnframe, text="Generate Bill", bg="cadetblue", command=self.bill_area,
                        fg="white", pady=15, width=10, font="arial 14 bold", bd=5)
        bgbill.grid(row=0, column=1, padx=10, pady=10)

        bclear = Button(btnframe, text="Clear", command=self.clear_data, bg="cadetblue",
                        fg="white", pady=15, width=10, font="arial 14 bold", bd=5)
        bclear.grid(row=0, column=2, padx=10, pady=10)

        bexit = Button(btnframe, text="Exit", command=self.exit_, bg="cadetblue",
                       fg="white", pady=15, width=10, font="arial 14 bold", bd=5)
        bexit.grid(row=0, column=3, padx=10, pady=10)
        self.welcome_bill()

    def total(self):
        # cosmetics
        self.csoap_price = self.soap.get()*40
        self.cfcprice = self.fc.get()*120
        self.cfwprice = self.fw.get()*60
        self.chsprice = self.spray.get()*180
        self.chgprice = self.gell.get()*140
        self.clotionprice = self.lotion.get()*180

        self.total_cosmetic_price = float(
            self.csoap_price +
            self.cfcprice +
            self.cfwprice +
            self.chsprice +
            self.chgprice +
            self.clotionprice
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05), 2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        # grocery
        self.griceprice = self.rice.get()*80
        self.gfoodoilprice = self.food_oil.get()*120
        self.gdaalprice = self.daal.get()*80
        self.gwheatprice = self.wheat.get()*120
        self.gsugarprice = self.sugar.get()*60
        self.gteaprice = self.tea.get()*50

        self.total_grocery_price = float(
            self.griceprice +
            self.gfoodoilprice +
            self.gdaalprice +
            self.gwheatprice +
            self.gsugarprice +
            self.gteaprice
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.10), 2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        # drinks
        self.dmaazap = (self.maaza.get()*40)
        self.dcockp = (self.cock.get()*120)
        self.dfrootip = (self.frooti.get()*60)
        self.dthumbsup = (self.thumbsup.get()*80)
        self.dlimcap = (self.limca.get()*60)
        self.dspritep = (self.sprite.get()*80)

        self.total_drinks_price = float(
            self.dmaazap +
            self.dcockp +
            self.dfrootip +
            self.dthumbsup +
            self.dlimcap +
            self.dspritep
        )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price*0.05), 2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_drinks_price +
            self.c_tax +
            self.g_tax +
            self.d_tax
        )

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWelcome Awesome Retail\n")
        self.textarea.insert(END, f"\nBill Number : {self.billno.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n=====================================")
        self.textarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n=====================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must!")

        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased!")

        else:
            self.welcome_bill()
            # ========================cosmetics======================================
            if self.soap.get() != 0:
                self.textarea.insert(
                    END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.csoap_price}")

            if self.fc.get() != 0:
                self.textarea.insert(
                    END, f"\n Face Cream\t\t{self.fc.get()}\t\t{self.cfcprice}")

            if self.fw.get() != 0:
                self.textarea.insert(
                    END, f"\n Face Wash\t\t{self.fw.get()}\t\t{self.cfwprice}")

            if self.spray.get() != 0:
                self.textarea.insert(
                    END, f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.chsprice}")

            if self.gell.get() != 0:
                self.textarea.insert(
                    END, f"\n Hair Gel\t\t{self.gell.get()}\t\t{self.chgprice}")

            if self.lotion.get() != 0:
                self.textarea.insert(
                    END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.clotionprice}")

            # ========================grocery======================================
            if self.rice.get() != 0:
                self.textarea.insert(
                    END, f"\n Rice\t\t{self.rice.get()}\t\t{self.griceprice}")

            if self.food_oil.get() != 0:
                self.textarea.insert(
                    END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.gfoodoilprice}")

            if self.daal.get() != 0:
                self.textarea.insert(
                    END, f"\n Daal\t\t{self.daal.get()}\t\t{self.gdaalprice}")

            if self.wheat.get() != 0:
                self.textarea.insert(
                    END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.gwheatprice}")

            if self.sugar.get() != 0:
                self.textarea.insert(
                    END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.gsugarprice}")

            if self.tea.get() != 0:
                self.textarea.insert(
                    END, f"\n Tea\t\t{self.tea.get()}\t\t{self.gteaprice}")

            # ========================Drinks======================================
            if self.maaza.get() != 0:
                self.textarea.insert(
                    END, f"\n Maaza\t\t{self.maaza.get()}\t\t{self.dmaazap}")

            if self.cock.get() != 0:
                self.textarea.insert(
                    END, f"\n Cock\t\t{self.cock.get()}\t\t{self.dcockp}")

            if self.frooti.get() != 0:
                self.textarea.insert(
                    END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.dfrootip}")

            if self.thumbsup.get() != 0:
                self.textarea.insert(
                    END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.dthumbsup}")

            if self.limca.get() != 0:
                self.textarea.insert(
                    END, f"\n Limca\t\t{self.limca.get()}\t\t{self.dlimcap}")

            if self.sprite.get() != 0:
                self.textarea.insert(
                    END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.dspritep}")

            self.textarea.insert(
                END, f"\n-------------------------------------")

            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.textarea.insert(
                    END, f"\nCosmetics Tax\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.textarea.insert(
                    END, f"\nGrocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.textarea.insert(
                    END, f"\nCold Drink Tax\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END, f"\nTotal Bill\t\tRs. {self.total_bill}")
            self.textarea.insert(
                END, f"\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        msg = messagebox.askyesno("Save Bill", "Do you want to save bill??")
        if msg > 0:
            self.bill_data = self.textarea.get('1.0', END)
            f = open("Bills/"+str(self.billno.get())+".txt", "w")
            f.write(self.bill_data)
            f.close()
            messagebox.showinfo(
                "Saved", f"Bill No. {self.billno.get()} saved successfully!")

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            # print(i)
            if i.split('.')[0] == self.search_bill.get():
                f = open(f"Bills/{i}", "r")
                self.textarea.delete('1.0', END)
                for j in f:
                    self.textarea.insert(END, j)
                f.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number!")

    def clear_data(self):
        # cosmetics
        self.soap.set(0)
        self.fc.set(0)
        self.fw.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.lotion.set(0)
        # grocery
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        # Cold Drink
        self.maaza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        # total product price and tax variable
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # customer
        self.c_name.set("")
        self.c_phone.set("")

        self.billno.set("")
        x = random.randint(1000, 9999)
        self.billno.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()

    def exit_(self):
        msg = messagebox.askyesno("Exit", "Do you really want to exit??")
        if msg > 0:
            self.root.destroy()


root = Tk()
ob = Bill(root)
root.mainloop()
