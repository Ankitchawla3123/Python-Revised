import new
new.newatt=3

print(new.newatt)
new.__dict__["hey"]=213
print(new.hey)


def extended_gcd(a, b):
    if b == 0:
        return a,1,0
    
    gcd,x1,y1=extended_gcd(b,a%b)
    x = y1
    y = x1-(a//b)*y1
    
    return gcd,x,y



a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))

if(a<b):
    print("error, a is less than b, 'a' must be > 'b'")
    exit()

gcd, x, y = extended_gcd(a, b)

print("GCD:", gcd)
print(" x:", x)
print(" y:", y)

print(f"{a}*({x}) + {b}*({y}) = {a*x + b*y}")
