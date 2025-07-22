from sympy import mod_inverse

def findP(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return 1
def text_number(text):
    return [ord(c)-ord('a')+1 for c in text]
def encrypt(text,e,n):
    num=text_number(text)
    return [pow(m,e,n) for m in num]


# Given values
n = 670726081
p = findP(n)
q = n // p  # use integer division

phi_n = (p - 1) * (q - 1)
d = 12345
text="hellodarknessmyoldfriend"
try:
    e = mod_inverse(d, phi_n)
    print(f"Public key exponent e = {e}")
except ValueError:
    print("Modular inverse does not exist.")
print(encrypt(text,e,n))