rent = int(input ("Enter your hostel/flat rent "))
food = int(input("Enter the amount of good enteed "))
electricity_spend =  int(input("Enter the amount of electricicty sped"))
charge_per_unit = int(input("Enter the charge per unit"))
persons = int(input("Enter hte number of prsons living in room/flat "))

total_bill = electricity_spend * charge_per_unit

output = (food +rent + total_bill)// persons
print(output)