def num_days(month):
    thirty_days = ['apr', 'jun', 'sep', 'nov']
    if month in thirty_days:
       days=30
    elif month == 'feb':
        days=28
    else:
        days=31
    return print(f"Number of days in month: {month} is {days} days")


month_name = input("Enter month abbreviation (e.g., jan, feb, mar): ").lower()
num_days(month_name)
