# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 06:27:57 2018

@author: Charan
"""
import pandas as pd

transactions = pd.DataFrame()

customerProfile = pd.DataFrame()

def inititalizeTransaction_df():
    global transactions
    print('Initalizing the Kitty Bank')
    dict2 = {'Custid':[101,102,103,104,105],
         'Transactionno':[21,22,23,24,25],
         'Date':['13/11/2018','13/11/2018','13/10/2018','10/11/2018','01/11/2018'],
         'Txn_type':[0,1,0,1,0],
         'Amount':[100000,10000,15000,5000,25000],
         'Balance':[100000,10000,15000,5000,25000]
    
        }   
    transactions=pd.DataFrame(data=dict2)
    
def initalizeCustomers_df():
    global customerProfile
    dict1 = {'Custid':[101,102,103,104,105,106],
         'Name':['Swetha','Swecha','Susmita','Sitara','Samanvi','Shlok'],
         'Age':[20,22,25,21,20,29],
         'City':['Hyd','Bng','Che','Kol','Coa','Goa'],
         'Gender':['F','F','F','F','F','M']
        }    
    customerProfile=pd.DataFrame(data=dict1)
    
def displayCustomerProfile():
    print('displayCustomerProfile')
    customerId = input('please enter  your customerId :')
    print(customerId)    
    for x in range(0,len(customerProfile)):
        if(customerProfile.iloc[x].loc['Custid']==int(customerId)):
            print('Customer Name is : {} and his balance is : {}'.format(customerProfile.iloc[x].loc['Name'],transactions.loc[transactions.Balance].loc['Balance']))
        
#Not requried to update in customer Details with amount 
def acceptDeposit1():
    print('AcceptDeposit')
    customerId = int(input('please enter  your customerId :'))
    amount =int(input('please enter  your amount :'))    
    customerProfile.loc[customerProfile['Custid']==customerId ,'Balance'] = customerProfile.loc[customerProfile['Custid']==customerId ,'Balance']+ amount
    print(customerProfile.loc[customerProfile['Custid']==customerId ,'Balance'])
    

def acceptDeposit():
    print('AcceptDeposit')
    customerId = int(input('please enter  your customerId :'))
    amount =int(input('please enter  your amount :'))    
    txno = max(transactions.Transactionno)+1
    previousbalance = transactions.loc[(transactions.Custid == customerId) & (transactions.Txn_type == 0),'Amount'].sum() - transactions.loc[(transactions.Custid == customerId) & (transactions.Txn_type == 1),'Amount'].sum()
    transactions.loc[max(transactions.index)+1] = [customerId,txno,'14/11/2018',0,amount,previousbalance+amount]


def addNewCustomer():
    print('Adding new customers')
    customerName = input('Please provide customer Name  :')
    age = int(input('Please provide your age: '))
    Gender = input('Please provide your gender: ')
    city = input('Please provide your city: ')    
    newCustomerId = max(customerProfile.Custid)+1
    customerProfile.loc[max(customerProfile.index)+1] = [newCustomerId,customerName,age,city,Gender]
    