#Program to calculate employee's gross and net pay
gross_pay = float(input("Enter the gross pay: "))
tax_rate=0.2
net_pay = gross_pay * (1 - tax_rate)
print("The gross pay is: %.2f" % gross_pay)
print("The net pay is: %.2f" % net_pay)
