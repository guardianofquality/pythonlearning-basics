ongoingAllowance = 200
savings = 3000
# add 100 to our current savings (Yeah!)
savings = savings + 100

# remove 50 from out ongoing allowance (Snif)
ongoingAllowance = ongoingAllowance - 50

# update the number of days we need to saveint 
numberOfDaysToSave = (5000 - ongoingAllowance) / 500

# update our ongoing allowance (again)
ongoingAllowance = ongoingAllowance + (30 - 10) * 7
print(ongoingAllowance, numberOfDaysToSave, ongoingAllowance)