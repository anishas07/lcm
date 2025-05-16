numLarge = int(input("Enter the largest number: "))
numSmall = int(input("Enter the smallest number: "))

a = numLarge
b = numSmall

while(numSmall):
    totalNum = numSmall
    numSmall = numLarge % numSmall
    numLarge = totalNum

lcm = (a * b) // numLarge
print("Here is the LCM:", lcm)