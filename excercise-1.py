# Where to put your Treasures

row1 = ["🧱","🧱","🧱"]
row2 = ["🧱","🧱","🧱"]
row3 = ["🧱","🧱","🧱"]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1]) 

# nested list
map = [row1, row2, row3]

# select row and column
map[row - 1][column - 1] = "🎁"

print(f"{row1}\n{row2}\n{row3}")