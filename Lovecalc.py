#LOVE CALCULATOR
print("!!Welcome to the love calculator!!")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")
name1_l = name1.lower()
name2_l = name2.lower()
key = name1_l + name2_l
count_pv10 = 0
count_pv10 += key.count("t")
count_pv10 += key.count("r")
count_pv10 += key.count("u")
count_pv10 += key.count("e")
count_pv1 = 0
count_pv1 += key.count("l")
count_pv1 += key.count("o")
count_pv1 += key.count("v")
count_pv1 += key.count("e")

print(f"Your love percentage is {count_pv10}{count_pv1}%")

