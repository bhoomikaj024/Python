print("Welcomme to the Tip Calculater!")
bill = float(input("What was the total bill? : Rs."))
tip_perc = float(input("What percentage of the tip would you like to give? : "))
persons  = int(input("How many people to split the bill? : "))
tip = bill * (tip_perc/100)
total_amt = bill + tip
share = round(total_amt / persons, 2)

print(f"Each person should pay: Rs.{share}")
