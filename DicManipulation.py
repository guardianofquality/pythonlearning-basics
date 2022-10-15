months = {}
months["June"] = 6
months["September"] = 9
months["March"] = 5

# TODO Step 1 - Fix March with the proper value (3)
months["March"] = 3
# TODO Step 2 – remove June
months.pop("June")
# print the content of the dict :
print("Here are some interesting months")
for month in months:
	print(month, " is month number ", months[month], " of the year ")