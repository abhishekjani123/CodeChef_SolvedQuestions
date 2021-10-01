n = int(input(“Enter any number: “))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print(“The number is a Perfect number”)
else:
    print(“The number is not a Perfect number”)
