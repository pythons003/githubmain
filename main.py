str1='welcome'
print(len(str1))

print(str1[2:4])

print(str1[1:])
print(str1[3:len(str1)])

print(str1[-1])
print(str1[-2])
 
print(str1[-3])
## to replace body with any
str2=str1+' every body'
print(str2)

str2=str1[0:]+' any'+str2[14:]
print(str2)
## to replace l with n
str3=str1[0:2]+'n'+str1[3:len(str1)]
print(str3)