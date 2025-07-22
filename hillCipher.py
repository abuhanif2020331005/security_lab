import numpy as  np
padsize=3
key_matrix=np.array([[6,24,1],[13,16,10],[20,17,15]])
def pad(text):
    t=len(text)%padsize
    if t==0:
      return text
    return 'x'*(padsize-t)+text
def text_vec(text):
    return np.array([ord(c) - ord('a') for c in text])
def vec_text(vec):
     return ''.join([chr((num %26)+ord('a')) for num in vec])
def hill_cipher(text):
    encrypted_text=''
    text=pad(text)
    print(f"plaintext:{text}")
    for i in range(0,len(text),padsize):
        segment=text[i:i+padsize]
        vector=text_vec(segment)
        encrypted_vec=key_matrix.dot(vector) % 26
        encrypted_text+=vec_text(encrypted_vec)
    return encrypted_text
text='paymoremoney'
encrypt=hill_cipher(text)
print(f"encrypt text:{encrypt}")    