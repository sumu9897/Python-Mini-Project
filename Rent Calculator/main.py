
rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in flat = "))

electricity_bill = electricity_spend * charge_per_unit

result = (food + rent + electricity_bill) // persons

print("Each person will pay = ", result)
