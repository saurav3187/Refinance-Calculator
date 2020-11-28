# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:31:53 2019

@author: Lenovo
"""

from tkinter import *
import numpy as np

class RefiEval:
    def __init__(self):
        window=Tk()
        window.title("Finance Evaluator")
        window.configure(bg="black")
        # loan inputs
        
        Label(window,text="Loan Amount: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=1,column=1,sticky=W)
        Label(window,text="Interest Rate: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=2,column=1,sticky=W)
        Label(window,text="Term (years): ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=3,column=1,sticky=W)
        Label(window,text=None,
              cnf={'fg':'white','bg':'black'}).grid(row=4,column=1,sticky=W)
        
        # outputs
        Label(window,text="Total Interest: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=5,column=1,sticky=W)
        Label(window,text="Total Amount To Be Paid: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=6,column=1,sticky=W)
        # variable to store  inputs
        
        self.pv=StringVar()
        self.interest_rate=StringVar()
        self.term=StringVar()
        # var for pmt output
        self.pmt=StringVar()
        self.total=StringVar()
        
        Entry(window,textvariable=self.pv,
              justify=RIGHT).grid(row=1,column=2,padx=(0,5))
        
        Entry(window,textvariable=self.interest_rate,
              justify=RIGHT).grid(row=2,column=2,padx=(0,5))
 
        Entry(window,textvariable=self.term,
              justify=RIGHT).grid(row=3,column=2,padx=(0,5))  
        
        Label(window,textvariable=self.pmt,
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 12 bold"
              ,justify=RIGHT).grid(row=5,column=2,sticky=E)
        
        Label(window,textvariable=self.total,
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 12 bold"
              ,justify=RIGHT).grid(row=6,column=2,sticky=E)
        
        
        Button(window,text="Calculate Payment",
               cnf={'fg':'blue','bg':'grey'},
               command=self.calcPayment,font="Helvetica 14").grid(row=7,column=2,padx=(100,5),pady=5)
                
        # refinance variable
        self.p=StringVar()
        self.t=StringVar()
        self.r=StringVar()
        self.n=StringVar()
        
        Label(window,text="Initial principal balance",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=8,column=1,sticky=W)
        
        Label(window,text="Number of time periods elapsed",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16",justify=RIGHT).grid(row=9,column=1,sticky=W)
        
        Label(window,text="Interest Rate",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16",justify=RIGHT).grid(row=10,column=1,sticky=W)
        
        Label(window,text="Number of times interest applied per time period",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16",justify=RIGHT).grid(row=11,column=1,sticky=W)
        
        # evaluation entries
        Entry(window,textvariable=self.p,
              justify=RIGHT).grid(row=8,column=2,padx=(0,5))
        
        Entry(window,textvariable=self.t,
              justify=RIGHT).grid(row=9,column=2,padx=(0,5))
         
        Entry(window,textvariable=self.r,
              justify=RIGHT).grid(row=10,column=2,padx=(0,5))
        
        Entry(window,textvariable=self.n,
              justify=RIGHT).grid(row=11,column=2,padx=(0,5))
        
        # output variable for evaluation
        self.amount=StringVar()
        self.interest=StringVar()
        
        Label(window,text="Total Amount: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=12,column=1)
        Label(window,text="Total Interest generated: ",
              cnf={'fg':'white','bg':'black'},
              font="Helvetica 16").grid(row=13,column=1)
        
        Label(window,textvariable=self.amount,
              cnf={'fg':'red'},
              font="Helvetica 12 bold"
              ,justify=RIGHT).grid(row=12,column=2,sticky=E)
        
        Label(window,textvariable=self.interest,
              font="Helvetica 12 bold"
              ,justify=RIGHT).grid(row=13,column=2,sticky=E)
        
        
        Button(window,text="Calculate Amount(Compound Interest rate)",
               cnf={'fg':'blue','bg':'grey'},
                font="Helvetica 14",command=self.compound_int).grid(row=14,column=2)
        window.mainloop()
        
        
    def calcPayment(self):
            pv=float(self.pv.get())
            rate=float(self.interest_rate.get())
            term=int(self.term.get())
            
            pmt=((pv*term*rate)/100)
            total=pmt+pv
            self.pmt.set("RS "+format(pmt,"5,.2f"))
            self.total.set("RS "+format(total,"8,.2f"))
            
            
    
            
    def compound_int(self):
        
        # perform comparison
        pi=float(self.p.get())
        ti=float(self.t.get())
        ni=float(self.n.get())
        ri=float(self.r.get())
        ri=ri/100
        
        amount=pi*((1+(ri/ni))**(ni*ti))
        interest=amount-pi

        self.amount.set("Rs"+ format(amount,"5.2f"))
    
        self.interest.set("Rs"+format(interest,"8,.2f"))
        
RefiEval( )
        