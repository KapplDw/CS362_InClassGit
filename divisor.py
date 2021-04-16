# Base File

# Ask for value start at 1 to value
# Mod value by i if 0 is divisor


value = int(input("Enter the value you would like to find Divisors for: "))

temp =[]
for i in range(1, value + 1):
    if (value % i == 0):
        temp.append(i)

print("Divisors are: " + str(temp) )
