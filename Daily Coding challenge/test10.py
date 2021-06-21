n=int(input("Enter the value of units: "))
if(n>=0 and n<=100):
    n=n*0
    print(n)
elif(n>100 and n<=200):
    n=(n-100)*1.5
    print(n)
elif(n>200 and n<=400):
    n=((n-200)*2.5)+150
    print(n)
elif(n>400):
    n=((n-400)*5)+650
    print(n)
else:
    print("Enter a valid number")
