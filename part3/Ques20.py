str1 = input("Enter first string:  ")
str2 = input("Enter second string: ")

i = 0 
while i<len(str1) and i<len(str2):
    if str1[i] > str2[i]:
     print(str1, "is lexicographically larger ")
     break

    elif str1[i] < str2[i]:
     print(str2,"is lexicographically larger")
     break
    else:
     i = i+1

else:
   if len(str1) > len(str2):
     print(str1, "is lexicographically larger ")
    
   elif len(str1) < len(str2):
     print(str2,"is lexicographically larger")

   else:
      print("Both strings are same")   
    