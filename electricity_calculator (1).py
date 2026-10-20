# Electricity Bill Calculator
RATE = 12.90

# name validation
name = input("Enter customer name: ")
if name.strip() == "":
  print("Invalid name. Please try again.")
  name = input("Enter customer name: ")

# number verification
previous = float(input("Enter previous meter reading: "))
if not previous.isdigit() or not (0 <= int(previous)):
  print("Invalid number. Enter a number equal or greater than 0.")
  previous = float(input("Enter previous meter reading: "))
  
# making sure current reading => previous reading
current = float(input("Enter current meter reading: "))
if current < previous:
  print("Invalid value. Current must be equal or greater than the previous.")
  current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
