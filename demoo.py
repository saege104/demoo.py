def calculate_tip(bill, percent):
    tip = bill * (percent / 100)
    return tip

bill_amount = float(input("What is your bill?"))
tip_percent = float(input("What percent do you want to tip"))

tip = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip

print(f"Tip amount: #{tip}")
print(f"Total to pay: #{total}")