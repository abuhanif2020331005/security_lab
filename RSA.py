def findP(n):
    for i in range(2,n+1):
        if(n%i ==0):
            return i
    return 1
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)
def find_modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse of {a} modulo {m} does not exist.")
    return x % m
def text_to_numbers(text):
    return [ord(c) - ord('a') + 1 for c in text]

def rsa_encrypt_message(message, e, n):
    nums = text_to_numbers(message)
    return [pow(m, e, n) for m in nums]
n=670726081
p=findP(n)
q=int(n/p)
print(p)
print(q)
phi_n = (p - 1) * (q - 1)
d=12345
e = find_modular_inverse(d,phi_n)
print(e)
m = "hellodarknessmyoldfriend"
print(rsa_encrypt_message(m,e,n))
