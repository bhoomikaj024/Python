row1 = ["🔲", "🔲", "🔲"]
row2 = ["🔲", "🔲", "🔲"]
row3 = ["🔲", "🔲", "🔲"]
map = [row1, row2, row3]
print("Enter the position you want to put the treasure at in the 3*3 grid.")
row = int(input("Enter the row: "))
col = int(input("Enter the column: "))
map[row-1][col-1] = "🪙"
print(f"{row1}\n{row2}\n{row3}")
