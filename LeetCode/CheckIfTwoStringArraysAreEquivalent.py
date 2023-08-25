# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
word1 = ["ab", "c"]
word2 = ["a", "bc"]
myvalue = ""  # Initialize myvalue as an empty string
myvalue2 = ""  # Initialize myvalue as an empty string
for i in word1:
    myvalue += i
print(myvalue)
for j in word2:
    myvalue2 += j
print(myvalue2)
if myvalue == myvalue2:
    {
        print("true")
    }
else:
    {
        print("false")
    }