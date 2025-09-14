sen = input("Enter a sentance:  ")

length = len(sen)
mid = length // 2 

firsthalf = sen[:mid]
secondhalf = sen[mid:]

print("First half is:",firsthalf)
print("Second half is:",secondhalf)
