from sympy import mod_inverse

def findP(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return 1
def text_number(text):
    return [ord(c)-ord('a')+1 for c in text]
def numbers_to_text(numbers):
    return ''.join([chr(n + ord('a') - 1) for n in numbers])
def encrypt(text,e,n):
    num=text_number(text)
    return [pow(m,e,n) for m in num]
def rsa_decrypt_message(cipher, d, n):
    decrypted_nums = [pow(c, d, n) for c in cipher]
    return numbers_to_text(decrypted_nums)

    

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
m=encrypt(text,e,n)
print(rsa_decrypt_message(m,d,n))