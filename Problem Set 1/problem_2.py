c = 0
left = 0
right = 3
s = 'azcbobobegghakl'
for i in range(len(s)):
    if s[left:right] == "bob":
        c+=1
    left+=1
    right+=1
print(c)