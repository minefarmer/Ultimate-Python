print("Enter hours worked")  # 45
hoursWorked = int(raw_input())
rate = 25.00
if hoursWorked > 40:
    grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
else:
    grossPay = hoursWorked * rate
print ('Gross pay: ' + str(grossPay))  # 1187.5