# Uses python3


def gcd(a,b): 
    if b == 0: 
        return a 
    return gcd(b, a%b) 
  

def lcm(a,b): 
    return int((a*b) / gcd(a,b))
a, b =list(map(int,input().split()))
print(lcm(a, b))

