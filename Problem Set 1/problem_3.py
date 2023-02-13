ans = []
s = 'abcdefghijklmnopqrstuvwxyz'
list1 = []
list1[:0] = s
left = 0
for right in range(len(list1)):
    if list1[left:right+1] == (sorted(list1[left:right+1])):
        if len(list1[left:right+1])>len(ans):
            ans = list1[left:right+1]
    else:
        while list1[left:right+1] != (sorted(list1[left:right+1])) and left < right:
            left+=1
final  =""
for i in ans:
    final+=i

print("longest string in alphabetical order is " + final)
