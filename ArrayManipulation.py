# TODO Step 1 - Replace the ?? by the proper code to create an empty list
guests = []

# TODO Step 2 - Add Joey, Martin and Marie to the list
guests.append("Joey")
guests.append("Martin")
guests.append("Marie")
# TODO Step 3 – display the size of the list
print(len(guests))
# TODO Step 4 - Replace Martin with John in the list
guests.pop(1)
guests.insert(1,"John")
# TODO Step 5 - Remove Joey from the list
guests.remove("Joey")

# print the content of the list
for guest in guests :
	print(guest)