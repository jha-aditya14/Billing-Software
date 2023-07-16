from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software".center(420))
        bg_color="#074463" 
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30, "bold"),pady=2).pack(fill=X)
        
        #-----Variables-----#
      
          
        #------Cosmetics Variable-------#
        
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.Loshan=IntVar()
        
        #-------grossary variable-------#
        
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        
        #-----------softdrink variable--------#
        
        self.maza=IntVar()
        self.fanta=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        #---- Total Product & Tax Variable--------#
        
        self.cosmetic_price=StringVar()
        self.grossary_price=StringVar()
        self.soft_drink_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grossary_tax=StringVar()
        self.soft_drink_tax=StringVar()
        
        #------Customer------#
        
        self.c_name=StringVar()
        self.c_phno=IntVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        
        #-----Customer Detail Frame-----" 
                
        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=0,padx=20,pady=20)
        cname_txt=Entry(F1,width = 15, textvariable=self.c_name,font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=20)
        cphn_txt=Entry(F1,width = 15, textvariable=self.c_phno, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=4,padx=20,pady=20)
        cbill_txt=Entry(F1,width = 15, textvariable=self.search_bill, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)


        bill_btn=Button(F1, text="Search", command=self.find, width=10,bd=7,font="arial 12 bold", cursor="hand2").grid(row=0,column=6, pady=10, padx=15)
        
        #------Cosmetics Frame-----#

        F2=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=192,width=325, height=365)
        
        c1_lbl=Label(F2, text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1=Entry(F2,width=10, textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  
         
        c2_lbl=Label(F2, text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F2,width=10, textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)  
        
        c3_lbl=Label(F2, text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F2,width=10, textvariable=self.face_wash, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        c4_lbl=Label(F2, text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F2,width=10, textvariable=self.spray, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)  
        
        c5_lbl=Label(F2, text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F2,width=10, textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)  
        
        c6_lbl=Label(F2, text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F2,width=10, textvariable=self.Loshan, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)  
        
        ##-------Grosary-------# 
        
        F3=LabelFrame(self.root, bd=10, relief=GROOVE, text="Grossary",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=192,width=325, height=365)
        
        g1_lbl=Label(F3, text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  
         
        g2_lbl=Label(F3, text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)  
        
        g3_lbl=Label(F3, text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3=Entry(F3,width=10, textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        g4_lbl=Label(F3, text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10, textvariable=self.wheat, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)  
        
        g5_lbl=Label(F3, text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10, textvariable=self.sugar, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)  
        
        g6_lbl=Label(F3, text="Tea and Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10, textvariable=self.tea, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)  
        
        #----------SoftDrinks-------------#
         
        F4=LabelFrame(self.root, bd=10, relief=GROOVE, text="Soft Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=192,width=325, height=365)
        
        sf1_lbl=Label(F4, text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sf1_txt=Entry(F4,width=10,textvariable=self.maza, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  
         
        sf2_lbl=Label(F4, text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sf2_txt=Entry(F4,width=10, textvariable=self.fanta, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)  
        
        sf3_lbl=Label(F4, text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sf3_txt=Entry(F4,width=10,textvariable=self.frooti, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        sf4_lbl=Label(F4, text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sf4_txt=Entry(F4,width=10,textvariable=self.thumbs_up, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)  
        
        sf5_lbl=Label(F4, text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sf5_txt=Entry(F4,width=10, textvariable=self.limca, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)  
        
        sf6_lbl=Label(F4, text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sf6_txt=Entry(F4,width=10, textvariable=self.sprite, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)  
        
        
        #---------Bill Area----------#
        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010,y=192,width=340, height=360)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #--------Button Frame---------# 

        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18, textvariable=self.cosmetic_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Grossary Price",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18, textvariable=self.grossary_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl=Label(F6,text="Total Soft Drink Price",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18, textvariable=self.soft_drink_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18, textvariable=self.cosmetic_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Grossary Tax",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18, textvariable=self.grossary_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(F6,text="Soft Drink Tax",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18, textvariable=self.soft_drink_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
       
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=585, height=105)
        
        
        total_btn=Button(btn_F, command=self.total, text="Total", bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        
    def total(self):
        if self.c_name.get()=="" or self.c_phno.get()=="":
                messagebox.showerror("Error","Customer details are must!!")
        else:        
            self.c_s_p=self.soap.get()*40
            self.c_fc_p=self.face_cream.get()*180
            self.c_fw_p=self.face_wash.get()*89
            self.c_hs_p=self.spray.get()*229
            self.c_hg_p=self.gel.get()*153
            self.c_bl_p=self.Loshan.get()*199

            self.g_r_p=self.rice.get()*85
            self.g_f_p=self.food_oil.get()*120
            self.g_d_p=self.daal.get()*60
            self.g_w_p=self.wheat.get()*245
            self.g_s_p=self.sugar.get()*51
            self.g_t_p=self.tea.get()*211
            
            self.sd_m_p=self.maza.get()*65
            self.sd_f_p=self.fanta.get()*60
            self.sd_fr_p=self.frooti.get()*65
            self.sd_t_p=self.thumbs_up.get()*65
            self.sd_l_p=self.limca.get()*58
            self.sd_s_p=self.sprite.get()*60


            self.total_cosmetic_price=float(
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hs_p+
                                            self.c_hg_p+
                                            self.c_bl_p
                                            )
            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
            self.c_tax=self.total_cosmetic_price*0.05
            self.cosmetic_tax.set("Rs. "+str(round((self.c_tax),2)))
                        
            self.total_grossary_price=float(
                                            self.g_r_p+
                                            self.g_f_p+
                                            self.g_d_p+
                                            self.g_w_p+
                                            self.g_s_p+
                                            self.g_t_p
                                            )
                                                            
            self.grossary_price.set("Rs. "+str(self.total_grossary_price))
            self.g_tax=self.total_grossary_price*0.02
            self.grossary_tax.set("Rs. "+str(round((self.g_tax),2)))

            self.total_soft_drinks_price=float(
                                                self.sd_m_p+
                                                self.sd_f_p+
                                                self.sd_fr_p+
                                                self.sd_t_p+
                                                self.sd_l_p+
                                                self.sd_s_p
                                            )
            self.soft_drink_price.set("Rs. "+str(self.total_soft_drinks_price))
            self.sd_tax=self.total_soft_drinks_price*0.019
            self.soft_drink_tax.set("Rs. "+str(round((self.sd_tax),2)))

            self.total_bill=float(self.g_tax+self.sd_tax+self.c_tax+self.total_cosmetic_price+self.total_grossary_price+self.total_soft_drinks_price)


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Aditya Retail\n")
        self.txtarea.insert(END, f"\nBill Number :{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number :{self.c_phno.get()} ")
        self.txtarea.insert(END, f"\n*************************************")
        self.txtarea.insert(END, f"\nProducts\t\t  Qty\t\tPrice")
        self.txtarea.insert(END, f"\n*************************************")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phno.get()=="":
            messagebox.showerror("Error","Customer details are must!!")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grossary_price.get()=="Rs. 0.0" and self.soft_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product purchased")

        
        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\nBath Soap\t\t  {self.soap.get()}\t   Rs. {self.c_s_p}")
            
            if self.face_cream.get()!=0: 
                self.txtarea.insert(END, f"\nFace Cream\t\t  {self.face_cream.get()}\t   Rs. {self.c_fc_p}")
                
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\nFash Wash\t\t  {self.face_wash.get()}\t   Rs. {self.c_fw_p}")
                
            if self.spray.get()!=0: 
                self.txtarea.insert(END, f"\nSpray\t\t  {self.spray.get()}\t   Rs. {self.c_hs_p}")
                
            if self.gel.get()!=0: 
                self.txtarea.insert(END, f"\nGel\t\t  {self.gel.get()}\t   Rs. {self.c_hg_p}")
                
            if self.Loshan.get()!=0:
                self.txtarea.insert(END, f"\nLoshan\t\t  {self.Loshan.get()}\t   Rs. {self.c_bl_p}")
        
        #--------------------------------------------------#

            if self.rice.get()!=0:
                self.txtarea.insert(END, f"\nRice\t\t  {self.rice.get()}\t   Rs. {self.g_r_p}")
            
            if self.food_oil.get()!=0: 
                self.txtarea.insert(END, f"\nFood Oil\t\t  {self.food_oil.get()}\t   Rs. {self.g_f_p}")

            if self.daal.get()!=0:
                self.txtarea.insert(END, f"\nDaal\t\t  {self.daal.get()}\t   Rs. {self.g_d_p}")
            
            if self.wheat.get()!=0: 
                self.txtarea.insert(END, f"\nWheat\t\t  {self.food_oil.get()}\t   Rs. {self.g_w_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END, f"\nSugar\t\t  {self.sugar.get()}\t   Rs. {self.g_s_p}")
            
            if self.tea.get()!=0: 
                self.txtarea.insert(END, f"\nFood Oil\t\t  {self.tea.get()}\t   Rs. {self.g_t_p}")
                
            
    #------------------------------------------------------------------#

            if self.maza.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.maza.get()}\t   Rs. {self.sd_m_p}")
            
            if self.fanta.get()!=0:
                self.txtarea.insert(END, f"\nFanta\t\t  {self.fanta.get()}\t   Rs. {self.sd_f_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END, f"\nFrooti\t\t  {self.frooti.get()}\t   Rs. {self.sd_fr_p}")
            
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END, f"\nThumbs Uo\t\t  {self.thumbs_up.get()}\t   Rs. {self.sd_t_p}")
            
            if self.limca.get()!=0:
                self.txtarea.insert(END, f"\nLimca\t\t  {self.limca.get()}\t   Rs. {self.sd_l_p}")
            
            if self.sprite.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.sprite.get()}\t   Rs. {self.sd_s_p}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")


            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t   {self.cosmetic_tax.get()}")
            
            if self.grossary_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nGrossary Tax\t\t\t   {self.grossary_tax.get()}")
            
            if self.soft_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nSoft Drink Tax\t\t\t   {self.soft_drink_tax.get()}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\tRs. {str(self.total_bill)}")
            
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesnocancel("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END) 
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
                    
    def clear_data(self):

        op=messagebox.askyesnocancel("Clear","Do you really want to Clear?")   
        if op>0:
            
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.Loshan.set(0)
            
            #-------grossary variable-------#
            
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            
            #-----------softdrink variable--------#
            
            self.maza.set(0)
            self.fanta.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            
            #---- Total Product & Tax Variable--------#
            
            self.cosmetic_price.set("")
            self.grossary_price.set("")
            self.soft_drink_price.set("")
            
            self.cosmetic_tax.set("")
            self.grossary_tax.set("")
            self.soft_drink_tax.set("")
            
            #------Customer------#
            
            self.c_name.set("")
            self.c_phno.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str())

    def Exit_app(self):
        op=messagebox.askyesnocancel("Exit","Do you really want to exit?")   
        if op>0:
            self.root.destroy()

       
root = Tk()
obj = Bill_App(root)
root.mainloop()
