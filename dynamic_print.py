import random
#The program of string format
unit_price = 70.56
quantity = 30
sales_tax_rate = 0.065
subtotal = unit_price * quantity
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
#start format
output = f""" 
Subtotal:   ${subtotal:>9,.2f}
Sales tax:  ${sales_tax:>9,.2f}
Total:      ${total:>9,.2f}
""" #end of format
print(output) #print
