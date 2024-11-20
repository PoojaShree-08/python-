#SIMPLEINTEREST
def simple_interest(p,t,r):
    si = (p * t * r)/100
    print('\nThe Simple Interest is', si,'\n')

P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)

#COMPOUNDINTREST
def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

compound_interest(10000, 10.25, 5)
