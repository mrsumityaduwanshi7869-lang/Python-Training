
p = int(input("Enter principle : "))
r = float(input("Enter rate of interest : "))
t = int(input("Enter time in months : "))

##    print simple interest
SI = (p*r*t)/100
print("Simple Interest = ",SI)

##    print compound interest

a1 = 1 + (r/100)
a = pow(a1, t)
A = p*a

CI = A - p
print("Compound interest = ",CI)
