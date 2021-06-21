n=int(input("Enter a number:"))
if(n<0):
    print("Negative range")
elif(n>=0 and n<=10):
    print("Low range")
elif(n>10 and n<=20):
    print("Med range")
elif(n>20 and n<=30):
    print("High range")
else:
    print("Extreme range")
