#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
operations = ["--X","X++","X++"]
x = 0

for operation in operations:
    if '+' in operation:
        x+=1
    else:
        x-=1

print(x)