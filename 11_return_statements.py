def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount + tax
    return total_amount
    #return amount, tax, total_amount #tuple
    #return [amount, tax, total_amount] #list
    #return {amount, tax, total_amount} #set
    #return f"{amount}, {tax}, {total_amount}"  #string
    
price = value_added_tax(100)    
print(price, type(price))