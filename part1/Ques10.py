str = input("Enter a string:  ")
length = len(str)

if length == 0:
    print("The string is empty")

elif length % 2 == 0:
     mid1 = length // 2-1
     mid2 = length // 2
     print("Middle two characters:", str[mid1]+str[mid2])

else :
     mid = length // 2
     print("Middle character:", str[mid])