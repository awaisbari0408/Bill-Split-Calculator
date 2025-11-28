print("Bill Split Calculator")

bill_amount = float(input("Please enter the Bill amount: "))
tip_percentage = float(input("What is the Tip Percentage on this Bill?\nTip Percentage: "))
number_of_people = int(input("How many people are paying this Bill?\nNumber of People: "))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / number_of_people

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${amount_per_person}")