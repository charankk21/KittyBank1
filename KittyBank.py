# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 06:58:26 2018

@author: Charan
"""

#intitalization
import pandas as pd

transactions = pd.DataFrame()

customerProfile = pd.DataFrame()

def addNewCustomer():
    print('Adding new customers')
    
def displayCustomerProfile():
    print('displayCustomerProfile')
    customerId = input('please enter  your customerId :')
    print(customerId)    
    for x in range(0,len(customerProfile)):
        if(customerProfile.iloc[x].loc['Custid']==int(customerId)):
            print('Customer Name is : {} and his balance is : {}'.format(customerProfile.iloc[x].loc['Name'],customerProfile.iloc[x].loc['Balance']))
      
def acceptDeposit():
    print('AcceptDeposit')
    customerId = int(input('please enter  your customerId :'))
    amount =int(input('please enter  your amount :'))    
    customerProfile.loc[customerProfile['Custid']==customerId ,'Balance'] = customerProfile.loc[customerProfile['Custid']==customerId ,'Balance']+ amount
    print(customerProfile.loc[customerProfile['Custid']==customerId ,'Balance'])
    
    
def withdrawMoney():
    print('Adding new withdrawMoney')
    
def customerPassbook():
    print('printing customerPassbook')
    
def dailyTellerStatement():
    print('dailyTellerStatement')
    
def Menu():
    print('Display menu')
    
def quitProgram():
    print('quitProgram')
    
    


def inititalizeTransaction_df():
    global transactions
    print('Initalizing the Kitty Bank')
    dict2 = {'Custid':[101,102,103,104,105],
         'Transactionno':[21,22,23,24,25],
         'Date':['13/11/2018','13/11/2018','13/10/2018','10/11/2018','01/11/2018'],
         'Txn_type':[0,1,0,1,0],
         'Amount':[100000,10000,15000,5000,25000]
    
        }   
    transactions=pd.DataFrame(data=dict2)
   
def initalizeCustomers_df():
    global customerProfile
    dict1 = {'Custid':[101,102,103,104,105,106],
         'Name':['Swetha','Swecha','Susmita','Sitara','Samanvi','Shlok'],
         'Age':[20,22,25,21,20,29],
         'City':['Hyd','Bng','Che','Kol','Coa','Goa'],
         'Gender':['F','F','F','F','F','M'],
         'Balance' : [0,0,0,0,0,0]
    
        }    
    customerProfile=pd.DataFrame(data=dict1)
 
    
switcher ={
        'n': addNewCustomer,
        'c': displayCustomerProfile,
        'd': acceptDeposit,
        'w': withdrawMoney,
        'p': customerPassbook,
        't': dailyTellerStatement,
        'm': Menu,
        'q': quitProgram
        }

options ='m'
switcher.get(options)()
while(options != 'q'):
    options = input('please enter  your options :')
    switcher.get(options)()


inititalizeTransaction_df()
initalizeCustomers_df()



customerProfile1 = ['107','Charan',29,'Hyd','M']

customerProfile.add(customerProfile1)




