## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# how many people living in room/flat

## Output
# Total amount you've to pay is
print("\n------ Rent Calculator ------")
Total_rent = int(input("Enter The Total Rent of your room/flat 🤔 = "))
food = int(input("Enter the total food amount 🍔🍕🍟 = "))
electricity = int(input("Enter the total of electricity spend/used 🔌🚃 = "))
charge_per_unit = int(input("Enter the charge per unit 💲= "))
roomamtes = int(input("Enter the total number of person living in the room/flat 🕴️🕴️ = "))


total_bill = electricity * charge_per_unit 

output = (Total_rent + food + total_bill ) // roomamtes

in_total= ( Total_rent + food + total_bill )

print(f"The Total Bill is : {in_total} and Each perosn has to pay : {output} ")

print("----------- Thanks -------------")