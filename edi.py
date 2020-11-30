import pandas as pd 
import os, csv
os.chdir("c:\\users\\pdinh\\python\\workediproj") #for working in shell
df = pd.read_csv("12927_9864490.csv")
#For "New Order at the top"
new_order = {"New Order"}
new_order_data = pd.DataFrame(new_order)
new_order_data.to_csv (r"c:\users\pdinh\python\workediproj\new_csv.csv", index=False, header=False)

#For customerOD
number = df["PartnerID"].values[0]
ODnumber = "OD"+str(number)
customer = {"customerNumber" : None,
            ODnumber: None}
customer_csv = pd.DataFrame(customer, index=[0])
customer_csv.to_csv ("new_csv.csv",mode="a", index=False)

#For PO#
po = df["Invoice"].values[0]
poNumber = {"PO": None,
            po: None}
po_csv = pd.DataFrame(poNumber, index=[0])
po_csv.to_csv ("new_csv.csv",mode="a", index=False)

#This part is for the Part# and quantity
partNu = df["PartNu"]
quantity = df["Quantity"]
new = {"Part" : partNu,
        "Quantity" : quantity}
new_csv = pd.DataFrame(new)
new_csv.to_csv ("new_csv.csv", mode="a", index=False, header=False)

of=pd.read_csv("new_csv.csv")
of=of.dropna()
of.to_csv("new_csv.csv")