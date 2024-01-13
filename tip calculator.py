print("welcome to the tip calculator")
bill = float(input("what was your total bill? $"))
tip = int(input("what percentage tip would you like to give? 10,12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_percent = tip/100
bill_with_tip = tip_percent * bill
total_bill = bill + bill_with_tip
each_person_bill = total_bill/people
final_bill = round(each_person_bill, 2)
final_bill = "{:.2f}".format(each_person_bill)
print(f"each person will pay ${final_bill}")

