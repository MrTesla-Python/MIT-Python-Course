num = 0
s = "afdsjfaoeafodsf"
for i in s:
    if i in "aeiou":
        num+=1
print("Number of vowels: " + str(num))