# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:44:56 2020

@author: Admin
"""

l=[]
m=[]

def user():
    
    name=input("Enter the name")
    name.upper()
    name=str1(name)             #name of user
    m.append(name)
    
    lastname=input("Enter the lastname")
    lastname.upper()
    lastname=str1(lastname)             #last name of user
    m.append(lastname)
    
    Age=input("Enter the your age")
    Age=age(Age)
    print(Age)
    print("AGE")
    m.append(Age)
    sch=schme(Age)
    m.append(sch)
    
    
    
    
    con=input("Enter the contact number")
    con=cont(con)                            #Contact number                       
    m.append(con)
    
    pin=input("Enter the pincode")
    pin=pincode(pin)                        #pincode
    m.append(pin)
    address=input("Enter the address")
    address.upper()
    m.append(address)
    
    l.append(m)
def str1(strin):                        #validation of name /last name
    if(strin.isalpha()==False):
        strin=input("Enter name again")     
        strin.upper()
        str1(strin)
    else:
        
        return strin
     
        
def cont(cont1):                          #validation of contact number              
    if(len(cont1)!=10):
        cont1=input("Enter contact number ")
        cont(cont1)
        
    elif(cont1.isnumeric()==False):
        cont1=input("Enter contact number")
        cont(cont1)
    else:
        return cont1
def pincode(pint):                         #validation of Pincode                 
    if(len(pint)!=6):
        pint=input("Enter the pincode")
        pincode(pint)
    elif(pint.isnumeric()==False):
         pint=input("Enter the pincode")
         pincode(pint)
    else:
        return pint
def age(age1):
    while(age1.isnumeric()==False or len(age1)<1 or int(age1)>=100 or len(age1)>3):
        age1=input("Enter the correct age")
    return(age1)
    #if(age1.isnumeric()==True and 1<=len(age1)<=3 and int(age1)<=100):
     #   print(age1)
      #  return(age1)
                    
        
            
    #else:
       # age1=input("Enter the correct age")
        #print(age1)
        #age(age1)
        
def schme(age1):
    
    
    if(1<=int(age1)<=12):
        
        print("01.$100 deposit and   discount upto 10%in school fees")
        print("02.$150 deposit and   discount upto 20%in school fees" )
        print("99.for no schems")
        sch=input("enter the schme number")
            
    elif(13<=int(age1)<=26):
        
        print("11.$100 deposit and   discount upto 10%in higher school fees")
        print("12.$150 deposit and   discount upto 20%in higher school fees" )
        print("99.for no schems")
        sch=input("enter the schme number")
    else:
        
        print("21.$100 deposit and   discount upto 10% in House loans")
        print("22.$150 deposit and   discount upto 20%in House loans" )
        print("99.for no schems")
        sch=input("enter the schme number")
            
    if(sch=="01"):
        return "discount upto 10%in school fees"
    elif(sch=="02"):
        return "discount upto 20%in school fees"
    elif(sch=="11"):
        return "discount upto 20%in higher school fees"
    elif(sch=="12"):
        return "discount upto 20%in higher school fees"
    elif(sch=="21"):
        return "discount upto 20%in House Loans "
    elif(sch=="22"):
        return "discount upto 20%in House Loans"
    elif(sch=="99"):
        return "No Scheme"
    else:
        return "No Scheme"
        
    
    
        
        
        
            
            
            
        
    
         
   

        
        
for i in range(3):
    user()
    
      
    
           
    
    

    
