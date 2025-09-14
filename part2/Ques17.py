word = input("Enter a word: ")

if word[0::] ==  word[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")