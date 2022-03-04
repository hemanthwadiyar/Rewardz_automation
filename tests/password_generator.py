import random


Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower = "abcdefghijklmnopqrstuvwxyz"
Number = "1234567890"
Symbol = "@#$!%*"

All = Upper+Lower+Number+Symbol
Len = int(input("Enter the length of password : "))

temp = random.sample(All,Len)
password = "".join(temp)

print(password)

