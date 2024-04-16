from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")





Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Times New Roman',50,'bold'),text=" Apni Haveli ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())

    if (Chilli_Chicken.get()==""):
        CoChilli_Chicken=0
    else:
        CoChilli_Chicken=float(Chilli_Chicken.get())

    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())


    if (Meals.get()==""):
        CoMeals=0
    else:
        CoMeals=float(Meals.get())


    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

    if (Kadhai_paneer.get()==""):
        CoKadhai_paneer=0
    else:
        CoKadhai_paneer=float(Kadhai_paneer.get())


    if (Paneer_chilli.get()==""):
        CoPaneer_chilli=0
    else:
        CoPaneer_chilli=float(Paneer_chilli.get())

    if (Handi_chicken.get()==""):
        CoHandi_chicken=0
    else:
        CoHandi_chicken=float(Handi_chicken.get())


    if (Grill_chicken.get()==""):
        CoGrill_chicken=0
    else:
        CoGrill_chicken=float(Grill_chicken.get())


    if (Tandoori_roti.get()==""):
        CoTandoori_roti=0
    else:
        CoTandoori_roti=float(Tandoori_roti.get())

    if (Plain_naan.get()==""):
        CoPlain_naan=0
    else:
        CoPlain_naan=float(Plain_naan.get())

    if (Butter_naan.get()==""):
        CoButter_naan=0
    else:
        CoButter_naan=float(Butter_naan.get())

    if (Garlic_naan.get()==""):
        CoGarlic_naan=0
    else:
        CoGarlic_naan=float(Garlic_naan.get())

    if (Plain_rice.get()==""):
        CoPlain_rice=0
    else:
        CoPlain_rice=float(Plain_rice.get())

    if (Jeera_rice.get()==""):
        CoJeera_rice=0
    else:
        CoJeera_rice=float(Jeera_rice.get())


    CostofJeera_rice = CoJeera_rice * 120
    CostofPlain_rice = CoPlain_rice * 80
    CostofGarlic_naan = CoGarlic_naan * 60
    CostofButter_naan = CoButter_naan * 50
    CostofPlain_naan = CoPlain_naan * 40
    CostofTandoori_roti = CoTandoori_roti * 15
    CostofGrill_chicken = CoGrill_chicken * 380
    CostofHandi_chicken = CoHandi_chicken * 240
    CostofPaneer_chilli = CoPaneer_chilli * 180
    CostofKadhai_paneer = CoKadhai_paneer * 170
    CostofChilli_Chicken = CoChilli_Chicken * 200
    CostofMeals =CoMeals * 150
    CostofFries =CoFries * 80
    CostofDrinks=CoD * 80
    CostofNoodles = CoNoodles * 100
    CostofSoup = CoSoup * 60
    CostBurger = CoBurger* 140
    CostSandwich=CoSandwich * 60

    CostofMeal= "₹", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofMeals+CostofChilli_Chicken+CostofKadhai_paneer+CostofPaneer_chilli+CostofHandi_chicken+CostofGrill_chicken+CostofTandoori_roti+CostofPlain_naan+CostofButter_naan+CostofGarlic_naan+CostofPlain_rice+CostofJeera_rice))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofMeals+CostofChilli_Chicken+CostofKadhai_paneer+CostofPaneer_chilli+CostofHandi_chicken+CostofGrill_chicken+CostofTandoori_roti+CostofPlain_naan+CostofButter_naan+CostofGarlic_naan+CostofPlain_rice+CostofJeera_rice) * 0.05)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofMeals+CostofChilli_Chicken+CostofKadhai_paneer+CostofPaneer_chilli+CostofHandi_chicken+CostofGrill_chicken+CostofTandoori_roti+CostofPlain_naan+CostofButter_naan+CostofGarlic_naan+CostofPlain_rice+CostofJeera_rice)
 
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofMeals+CostofChilli_Chicken+CostofKadhai_paneer+CostofPaneer_chilli+CostofHandi_chicken+CostofGrill_chicken+CostofTandoori_roti+CostofPlain_naan+CostofButter_naan+CostofGarlic_naan+CostofPlain_rice+CostofJeera_rice)/99)

    Service = "₹", str ('%.2f' % Ser_Charge)

    OverAllCost ="₹", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "₹", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    Meals.set("")
    Chilli_Chicken.set("")
    Kadhai_paneer.set("")
    Paneer_chilli.set("")
    Handi_chicken.set("")
    Grill_chicken.set("")
    Tandoori_roti.set("")
    Plain_naan.set("")
    Butter_naan.set("")
    Garlic_naan.set("")
    Plain_rice.set("")
    Jeera_rice.set("")


#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
Meals=StringVar()
Chilli_Chicken = StringVar()
Kadhai_paneer =StringVar()
Paneer_chilli =StringVar()
Handi_chicken = StringVar()
Grill_chicken = StringVar()
Tandoori_roti = StringVar()
Plain_naan = StringVar()
Butter_naan = StringVar()
Garlic_naan = StringVar()
Plain_rice = StringVar()
Jeera_rice = StringVar()




lblDrinks= Label(f1, font=('arial', 14, 'bold'),text="Pizza",bd=16,anchor="w")
lblDrinks.grid(row=2, column=0)
txtDrinks=Entry(f1, font=('arial',12,'bold'),textvariable=Meals,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtDrinks.grid(row=2,column=1)



lblFries= Label(f1, font=('arial', 14, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',12,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtFries.grid(row=1,column=1)





lblSoup= Label(f1, font=('arial', 14, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',12,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 14, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',12,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================


lblNoodles= Label(f1, font=('arial', 14, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=0, column=2)
txtNoodles=Entry(f1, font=('arial',12,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtNoodles.grid(row=0,column=3)


lblNoodles= Label(f1, font=('arial', 14, 'bold'),text="Kadhai Paneer",bd=16,anchor="w")
lblNoodles.grid(row=1, column=2)
txtNoodles=Entry(f1, font=('arial',12,'bold'),textvariable=Kadhai_paneer,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtNoodles.grid(row=1,column=3)

lblNoodles= Label(f1, font=('arial', 14, 'bold'),text="Paneer Chilli",bd=16,anchor="w")
lblNoodles.grid(row=2, column=2)
txtNoodles=Entry(f1, font=('arial',12,'bold'),textvariable=Paneer_chilli,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtNoodles.grid(row=2,column=3)

lblNoodles= Label(f1, font=('arial', 14, 'bold'),text="Handi Chicken",bd=16,anchor="w")
lblNoodles.grid(row=3, column=2)
txtNoodles=Entry(f1, font=('arial',12,'bold'),textvariable=Handi_chicken,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtNoodles.grid(row=3,column=3)

lblNoodles= Label(f1, font=('arial', 14, 'bold'),text="Grill Chicken",bd=16,anchor="w")
lblNoodles.grid(row=4, column=2)
txtNoodles=Entry(f1, font=('arial',12,'bold'),textvariable=Grill_chicken,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtNoodles.grid(row=4,column=3)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Chilli Chicken",bd=16,anchor="w")
lblSandwich.grid(row=5, column=2)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Chilli_Chicken,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=5,column=3)
#============================================================================================================
#                                RESTAURANT INFO 3
#========================================================================================



lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Tandoori Roti",bd=16,anchor="w")
lblSandwich.grid(row=0, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Tandoori_roti,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=0,column=5)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Plain Naan",bd=16,anchor="w")
lblSandwich.grid(row=1, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Plain_naan,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=1,column=5)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Butter Naan",bd=16,anchor="w")
lblSandwich.grid(row=2, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Butter_naan,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=2,column=5)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Garlic Naan",bd=16,anchor="w")
lblSandwich.grid(row=3, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Garlic_naan,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=3,column=5)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Plain Rice",bd=16,anchor="w")
lblSandwich.grid(row=4, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Plain_rice,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=4,column=5)

lblSandwich= Label(f1, font=('arial', 14, 'bold'),text="Jeera Rice",bd=16,anchor="w")
lblSandwich.grid(row=5, column=4)
txtSandwich=Entry(f1, font=('arial',12,'bold'),textvariable=Jeera_rice,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtSandwich.grid(row=5,column=5)





#============================================================================================================
#                                RESTAURANT INFO 4
#========================================================================================

lblDrinks= Label(f1, font=('arial', 14, 'bold'),text="Momos",fg = "black", bd=16,anchor="w")
lblDrinks.grid(row=0, column=0)
txtDrinks=Entry(f1, font=('arial',12,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtDrinks.grid(row=0,column=1)

lblCost= Label(f1, font=('arial', 14, 'bold'),text="Cost before Tax",bd=16,anchor="w")
lblCost.grid(row=2, column=8)
txtCost=Entry(f1, font=('arial',12,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtCost.grid(row=2,column=9)


lblService= Label(f1, font=('arial', 14, 'italic','bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=3, column=8)
txtService=Entry(f1, font=('arial',12,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtService.grid(row=3,column=9)


lblStateTax= Label(f1, font=('arial', 14, 'bold'),text="GST",bd=16,anchor="w")
lblStateTax.grid(row=4, column=8)
txtStateTax=Entry(f1, font=('arial',12,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtStateTax.grid(row=4,column=9)



lblTotalCost= Label(f1, font=('arial', 14, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=8)
txtTotalCost=Entry(f1, font=('arial',12,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtTotalCost.grid(row=5,column=9)


lblReference= Label(f1, font=('arial', 14, 'bold'),text="Invoice No.",bd=16,anchor="w")
lblReference.grid(row=1, column=8)
txtReference=Entry(f1, font=('arial',12,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="Sky blue",justify='right')
txtReference.grid(row=1,column=9)



#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="Sky blue",command=Ref).grid(row=7,column=2)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="Sky blue",command=Reset).grid(row=7,column=3)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="Sky blue",command=qExit).grid(row=7,column=4)





root.mainloop()


